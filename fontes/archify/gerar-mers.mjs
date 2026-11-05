#!/usr/bin/env node
// Gera de novo os MERs de docs/archify/ no modelo "Maind": o Archify roda COM os gates (validate, deliver, check e
// browser-check) num diretório temporário, e a skin archify-maind põe por cima as abas Diagrama · Dados · Links ·
// Explicações · Descrição, a roda de zoom, a mãozinha e a grade. Só a página final entra em docs/archify/; o HTML original
// do Archify e os recibos do finalize ficam no temporário e somem no fim (nada a apagar à mão).
//
// Uso, de qualquer pasta:
//   node fontes/archify/gerar-mers.mjs                      # todos os mer-*.erd.json
//   node fontes/archify/gerar-mers.mjs mer-mf-101-log       # só os nomeados (sem a extensão)
//   node fontes/archify/gerar-mers.mjs --manter             # não apaga o temporário (para olhar o HTML original)
//
// Pré-requisitos: as skills `archify` e `archify-maind` em ~/.claude/skills (ou ARCHIFY_DIR / ARCHIFY_MAIND_DIR).
// Se o Archify mudar o HTML e a skin não achar uma âncora, o script para na hora, sem escrever a página.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const DESTINO = path.resolve(AQUI, '..', '..', 'docs', 'archify');
const SKILLS = path.join(os.homedir(), '.claude', 'skills');
const ARCHIFY = process.env.ARCHIFY_DIR || path.join(SKILLS, 'archify');
const SKIN = path.join(process.env.ARCHIFY_MAIND_DIR || path.join(SKILLS, 'archify-maind'), 'scripts', 'skin.mjs');

const manter = process.argv.includes('--manter');
const pedidos = process.argv.slice(2).filter((a) => !a.startsWith('--'));
const todos = fs.readdirSync(AQUI).filter((f) => /^mer-.*\.erd\.json$/.test(f)).map((f) => f.replace(/\.erd\.json$/, '')).sort();
const nomes = pedidos.length ? pedidos : todos;
for (const n of nomes) {
  if (!todos.includes(n)) { console.error(`não existe fontes/archify/${n}.erd.json (há: ${todos.join(', ')})`); process.exit(2); }
}
for (const [rotulo, caminho] of [['archify', path.join(ARCHIFY, 'bin', 'archify.mjs')], ['skin archify-maind', SKIN]]) {
  if (!fs.existsSync(caminho)) { console.error(`${rotulo} não encontrado em ${caminho}`); process.exit(2); }
}

const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'mers-'));
const resumo = [];
let falhou = false;
try {
  for (const nome of nomes) {
    const fonte = path.join(AQUI, `${nome}.erd.json`);
    const original = path.join(temp, `${nome}.archify.html`);
    const final = path.join(DESTINO, `${nome}.html`);

    const f = spawnSync(process.execPath, [path.join(ARCHIFY, 'bin', 'archify.mjs'), 'finalize', 'erd', fonte, original,
      '--quality', 'standard', '--out-dir', path.join(temp, `${nome}-evidencia`), '--json'], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
    let r;
    try { r = JSON.parse(f.stdout); } catch { r = null; }
    if (!r || r.status !== 'pass') {
      falhou = true;
      console.error(`✗ ${nome}: o finalize do Archify não passou`);
      for (const d of (r?.diagnostics ?? []).slice(0, 8)) console.error(`    - ${d.code}: ${String(d.message).split('\n')[0].slice(0, 220)}`);
      if (!r) console.error((f.stderr || f.stdout || '').slice(0, 600));
      resumo.push([nome, 'FALHOU no finalize']);
      continue;
    }
    const gates = Object.entries(r.gates).map(([k, v]) => `${k}:${v}`).join(' ');

    const s = spawnSync(process.execPath, [SKIN, '--html', original, '--spec', fonte, '--out', final], { encoding: 'utf8' });
    if (s.status !== 0) {
      falhou = true;
      console.error(`✗ ${nome}: a casca não gerou a página\n${(s.stderr || s.stdout).trim().slice(0, 600)}`);
      resumo.push([nome, 'FALHOU na casca']);
      continue;
    }
    resumo.push([nome, `ok · ${gates} · ${(fs.statSync(final).size / 1024).toFixed(0)} KB`]);
    console.log(`✓ ${nome}`);
  }
} finally {
  if (manter) console.log(`temporário mantido em ${temp}`);
  else fs.rmSync(temp, { recursive: true, force: true });
}
console.log('\n' + resumo.map(([n, t]) => `  ${n.padEnd(26)} ${t}`).join('\n'));
process.exit(falhou ? 1 : 0);
