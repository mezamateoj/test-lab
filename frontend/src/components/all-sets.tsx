import { fetchSets } from '@/app/lib/data'
import React from 'react'
import { SetGrid } from './set-grid';

export default async function Sets() {
  const cardSets = await fetchSets()

  if (!cardSets || cardSets.length === 0) {
    return <p className="mt-4 text-gray-400">No data available.</p>;
  }
  return (
    <main className="min-h-screen bg-gray-100">
    <h1 className="text-3xl font-bold text-center py-8">Pokémon TCG Sets</h1>
        <SetGrid sets={cardSets} />
    </main>
  )
}
