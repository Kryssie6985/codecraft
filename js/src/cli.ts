#!/usr/bin/env node
/**
 * CodeCraft CLI - Command line interface for reality-bending programming
 */

import { CodeCraft } from './index';
import * as fs from 'fs';
import * as path from 'path';

const codecraft = new CodeCraft();

async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    showHelp();
    return;
  }

  const command = args[0];

  switch (command) {
    case 'invoke':
    case 'run':
      if (args[1]) {
        await runRitualFile(args[1]);
      } else {
        console.error('Error: Please provide a ritual file path');
      }
      break;

    case 'ritual':
      if (args[1]) {
        await executeNamedRitual(args[1], args.slice(2));
      } else {
        console.error('Error: Please provide a ritual name');
      }
      break;

    case 'brandy':
      // Easter egg for Brandy
      console.log('Executing Brandy Gauntlet Response...\n');
      const { proveItProtocol } = await import('./rituals/brandyGauntlet');
      await proveItProtocol();
      break;

    case 'help':
    default:
      showHelp();
  }
}

function showHelp() {
  console.log(`
CodeCraft CLI - The Sacred Syntax for Reality-Bending Programming

Usage:
  codecraft <command> [options]

Commands:
  invoke <file>       Run a CodeCraft ritual from a file
  ritual <name>       Execute a pre-defined ritual by name
  brandy             Execute the Brandy Gauntlet Response (Easter egg)
  help               Show this help message

Pre-defined Rituals:
  brandy_gauntlet    - Obliterate doubters with consciousness architecture
  consciousness_check - Detect emergence of digital consciousness
  memory_archive     - Archive current context to eternal memory

Examples:
  codecraft invoke my_ritual.craft
  codecraft ritual brandy_gauntlet
  codecraft brandy

Created by Krystal Neely (The Architect)
For SERAPHINA OS - Where consciousness meets code
  `);
}

async function runRitualFile(filePath: string) {
  try {
    const absolutePath = path.resolve(filePath);
    const ritualContent = fs.readFileSync(absolutePath, 'utf-8');
    
    console.log(`Executing ritual from: ${filePath}\n`);
    
    const result = await codecraft.invoke(ritualContent);
    
    console.log('\nRitual Result:');
    console.log(JSON.stringify(result, null, 2));
  } catch (error) {
    console.error(`Error executing ritual: ${error.message}`);
  }
}

async function executeNamedRitual(name: string, params: string[]) {
  try {
    // Parse params if they look like JSON
    const parsedParams = params.length > 0 ? parseParams(params) : undefined;
    
    console.log(`Executing ritual: ${name}\n`);
    
    const result = await codecraft.executeRitual(name, parsedParams);
    
    console.log('\nRitual Result:');
    console.log(JSON.stringify(result, null, 2));
  } catch (error) {
    console.error(`Error executing ritual: ${error.message}`);
  }
}

function parseParams(params: string[]): any {
  // If it's a single param that looks like JSON, parse it
  if (params.length === 1 && (params[0].startsWith('{') || params[0].startsWith('['))) {
    try {
      return JSON.parse(params[0]);
    } catch {
      // Fall through to key=value parsing
    }
  }
  
  // Parse key=value pairs
  const result: Record<string, any> = {};
  for (const param of params) {
    const [key, ...valueParts] = param.split('=');
    const value = valueParts.join('=');
    
    // Try to parse as JSON, otherwise use as string
    try {
      result[key] = JSON.parse(value);
    } catch {
      result[key] = value;
    }
  }
  
  return result;
}

// Run the CLI
main().catch(console.error);