'use server'

import { Card, Set } from "./definitions";

const url = `${process.env.NEXT_PUBLIC_API_URL}`

export async function fetchSets(): Promise<Set[]> {
    try {
        const res = await fetch(`${url}/api/sets/`)
        
        if (!res.ok) {
            throw new Error('Error fetching Set data')
        }
        const data = await res.json()

        // this should have a zod schema and validate the data before returning
        return data

    } catch (error) {
        throw new Error('Error')
    }
}


export async function fetchSetById(id: string): Promise<Card[]> {
    try {
        const res = await fetch(`${url}/api/sets/${id}/cards/`)
        
        if (!res.ok) {
            throw new Error('Error fetching Set data')
        }
        const data = await res.json()
        return data
    } catch (error) {
        throw new Error('Error')
    }
}




export async function fetchCardById(id: string): Promise<Card> {
    try {
        const res = await fetch(`${url}/api/cards/${id}/`)
        
        if (!res.ok) {
            throw new Error('Error fetching Set data')
        }
        const data = await res.json()

        return data

    } catch (error) {
        throw new Error('Error')
    }
}

