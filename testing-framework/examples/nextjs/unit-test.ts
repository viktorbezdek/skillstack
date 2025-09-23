import { describe, it, expect, beforeEach, vi } from 'vitest'

/**
 * Example unit test demonstrating best practices
 * for testing pure functions and business logic
 */

// Example function to test
function validateEntityName(name: string): { valid: boolean; error?: string } {
  if (!name || name.trim().length === 0) {
    return { valid: false, error: 'Name is required' }
  }
  if (name.length > 100) {
    return { valid: false, error: 'Name must be 100 characters or less' }
  }
  if (!/^[a-zA-Z0-9\s-_']+$/.test(name)) {
    return { valid: false, error: 'Name contains invalid characters' }
  }
  return { valid: true }
}

describe('validateEntityName', () => {
  it('accepts valid entity names', () => {
    expect(validateEntityName('John Doe').valid).toBe(true)
    expect(validateEntityName("O'Brien").valid).toBe(true)
    expect(validateEntityName('Location-123').valid).toBe(true)
  })

  it('rejects empty names', () => {
    const result = validateEntityName('')
    expect(result.valid).toBe(false)
    expect(result.error).toBe('Name is required')
  })

  it('rejects names with only whitespace', () => {
    const result = validateEntityName('   ')
    expect(result.valid).toBe(false)
    expect(result.error).toBe('Name is required')
  })

  it('rejects names exceeding max length', () => {
    const longName = 'a'.repeat(101)
    const result = validateEntityName(longName)
    expect(result.valid).toBe(false)
    expect(result.error).toContain('100 characters')
  })

  it('rejects names with invalid characters', () => {
    const result = validateEntityName('Name@#$')
    expect(result.valid).toBe(false)
    expect(result.error).toContain('invalid characters')
  })
})

// Example async function test
async function fetchEntityData(id: string): Promise<any> {
  const response = await fetch(`/api/entities/${id}`)
  if (!response.ok) throw new Error('Failed to fetch')
  return response.json()
}

describe('fetchEntityData', () => {
  beforeEach(() => {
    global.fetch = vi.fn()
  })

  it('fetches entity data successfully', async () => {
    const mockData = { id: '1', name: 'Test Entity' }
    ;(global.fetch as any).mockResolvedValueOnce({
      ok: true,
      json: async () => mockData
    })

    const result = await fetchEntityData('1')
    expect(result).toEqual(mockData)
    expect(global.fetch).toHaveBeenCalledWith('/api/entities/1')
  })

  it('throws error on failed fetch', async () => {
    ;(global.fetch as any).mockResolvedValueOnce({
      ok: false
    })

    await expect(fetchEntityData('1')).rejects.toThrow('Failed to fetch')
  })
})
