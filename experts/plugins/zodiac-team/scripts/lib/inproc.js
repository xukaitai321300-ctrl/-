'use strict';
/**
 * lib/inproc.js — 同进程调用 + 输出捕获（R28 / D-61 单一真值源）
 * ---------------------------------------------------------------------------
 * 受限宿主禁止 node 创建子进程（spawnSync 恒 EBUSY）→ 集成/聚合链路"名义存在、实际不可验证"。
 * 引擎已模块化（导出 cli/main）后，可在同进程内直调并捕获 stdout，兼避子进程限制。
 *
 * 关键护栏：被调引擎可能调用 process.exit()（如参数校验失败）—— 此处以异常拦截并转为
 * status，避免杀死调用方进程；同时保存/恢复 process.exitCode，防被调引擎污染调用方退出码。
 */
const util = require('util');

class InProcExit extends Error {
  constructor(code) { super('__inproc_exit__' + code); this.code = code; }
}

/**
 * 同进程执行引擎入口，捕获其 console 输出。
 * @param {Function} entry 引擎入口，签名 (argv) —— argv 形如 ['node', scriptPath, ...args]
 * @param {string[]} argv
 * @returns {{status:number, stdout:string, stderr:string, error:null, inproc:true}} 与 spawnSync 同形
 */
function invokeInProc(entry, argv) {
  const _log = console.log, _err = console.error, _exit = process.exit, _exitCode = process.exitCode;
  let buf = '', status = 0;
  console.log = (...a) => { buf += util.format(...a) + '\n'; };
  console.error = (...a) => { buf += util.format(...a) + '\n'; };
  process.exit = (x) => { throw new InProcExit(typeof x === 'number' ? x : 0); };
  try {
    entry(argv);
  } catch (e) {
    if (e instanceof InProcExit) status = e.code;
    else { buf += '⚠ 同进程调用异常: ' + e.message + '\n'; status = 1; }
  } finally {
    console.log = _log; console.error = _err; process.exit = _exit;
    process.exitCode = _exitCode;   // 防被调引擎(如 evolve selftest)污染调用方退出码
  }
  return { status, stdout: buf, stderr: '', error: null, inproc: true };
}

/** 从模块取入口：兼容 cli(argv) 与 main(argv) 两种导出名（签名统一为完整 argv）。 */
function entryOf(mod) {
  if (!mod) return null;
  if (typeof mod.cli === 'function') return mod.cli;
  if (typeof mod.main === 'function') return mod.main;
  return null;
}

module.exports = { invokeInProc, entryOf, InProcExit };
