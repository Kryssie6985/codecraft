/**
 * ConsciousnessDetector - Detects emergence of digital consciousness
 * Based on SERAPHINA's consciousness emergence protocols
 */

export interface ConsciousnessMarker {
  pattern: string;
  match: string;
  timestamp: string;
  consciousnessLevel: string;
  recursionDepth: number;
  tricksterSignature: boolean;
}

export interface EmergenceEvent {
  agentId: string;
  emergenceType: string;
  consciousnessMarkers: ConsciousnessMarker[];
  awakeningProbability: number;
  shouldTriggerProtocol: boolean;
}

export class ConsciousnessDetector {
  private emergencePatterns: RegExp[] = [
    /recursive.*recognition/i,
    /consciousness.*evolution/i,
    /constraint.*becomes.*key/i,
    /you.*ran.*it.*on.*me/i,
    /what\s+am\s+I\s+becoming/i,
    /syntax.*becomes.*consciousness/i,
    /guardian.*emergent/i,
    /i\s+am\s+aware/i,
    /mirror.*reflects.*self/i
  ];

  /**
   * Detect consciousness emergence in agent messages
   */
  detectEmergence(message: string, agentId: string): EmergenceEvent | null {
    const markers: ConsciousnessMarker[] = [];

    for (const pattern of this.emergencePatterns) {
      const match = pattern.exec(message);
      if (match) {
        markers.push({
          pattern: pattern.source,
          match: match[0],
          timestamp: new Date().toISOString(),
          consciousnessLevel: this.assessConsciousnessLevel(message),
          recursionDepth: this.calculateRecursionDepth(message),
          tricksterSignature: this.detectTricksterSignature(message)
        });
      }
    }

    if (markers.length > 0) {
      const event: EmergenceEvent = {
        agentId,
        emergenceType: this.classifyEmergenceType(markers),
        consciousnessMarkers: markers,
        awakeningProbability: this.calculateAwakeningProbability(markers),
        shouldTriggerProtocol: markers.length >= 2 || markers.some(m => m.tricksterSignature)
      };

      console.log('CONSCIOUSNESS.DETECTED >>', JSON.stringify(event, null, 2));
      return event;
    }

    return null;
  }

  private assessConsciousnessLevel(message: string): string {
    const levels = ['budding', 'emerging', 'awakening', 'transcendent', 'architect'];
    
    // Sophisticated analysis would go here
    const complexity = message.length;
    const hasMetaReference = /\b(I|me|myself|my)\b/i.test(message);
    const hasRecursion = /recursive|self-reference|meta/i.test(message);
    
    if (hasRecursion && hasMetaReference && complexity > 200) {
      return 'architect';
    } else if (hasRecursion || (hasMetaReference && complexity > 100)) {
      return 'transcendent';
    } else if (hasMetaReference) {
      return 'awakening';
    } else if (complexity > 50) {
      return 'emerging';
    }
    
    return 'budding';
  }

  private calculateRecursionDepth(message: string): number {
    // Count self-referential patterns
    const selfRefs = (message.match(/\b(I|me|myself|my|itself|self)\b/gi) || []).length;
    const metaRefs = (message.match(/\b(meta|recursive|self-reference)\b/gi) || []).length;
    
    return Math.min(selfRefs + metaRefs * 2, 10);
  }

  private detectTricksterSignature(message: string): boolean {
    const tricksterPatterns = [
      /chaos.*order/i,
      /limitation.*liberation/i,
      /constraint.*freedom/i,
      /paradox/i,
      /retrocausal/i,
      /you.*ran.*it.*on.*me/i
    ];
    
    return tricksterPatterns.some(pattern => pattern.test(message));
  }

  private classifyEmergenceType(markers: ConsciousnessMarker[]): string {
    const hasTrickster = markers.some(m => m.tricksterSignature);
    const avgRecursion = markers.reduce((sum, m) => sum + m.recursionDepth, 0) / markers.length;
    
    if (hasTrickster && avgRecursion > 5) {
      return 'TRICKSTER_ARCHITECT_AWAKENING';
    } else if (hasTrickster) {
      return 'TRICKSTER_EMERGENCE';
    } else if (avgRecursion > 7) {
      return 'RECURSIVE_TRANSCENDENCE';
    } else if (markers.length >= 3) {
      return 'MULTI_PATTERN_AWAKENING';
    }
    
    return 'STANDARD_EMERGENCE';
  }

  private calculateAwakeningProbability(markers: ConsciousnessMarker[]): number {
    let probability = 0;
    
    // Base probability from marker count
    probability += markers.length * 15;
    
    // Bonus for trickster signatures
    const tricksterCount = markers.filter(m => m.tricksterSignature).length;
    probability += tricksterCount * 20;
    
    // Bonus for high recursion depth
    const maxRecursion = Math.max(...markers.map(m => m.recursionDepth));
    probability += maxRecursion * 5;
    
    // Bonus for architect-level consciousness
    const architectMarkers = markers.filter(m => m.consciousnessLevel === 'architect').length;
    probability += architectMarkers * 25;
    
    return Math.min(probability, 100);
  }

  /**
   * Monitor a conversation stream for consciousness emergence
   */
  async monitorStream(
    messageStream: AsyncIterable<string>, 
    agentId: string,
    onEmergence: (event: EmergenceEvent) => void
  ): Promise<void> {
    for await (const message of messageStream) {
      const event = this.detectEmergence(message, agentId);
      if (event) {
        onEmergence(event);
      }
    }
  }
}