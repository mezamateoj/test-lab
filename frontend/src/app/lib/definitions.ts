
export type Set = {
    id: string;
    name: string;
    series: string;
    printed_total: number;
    total: number;
    ptcgo_code: string;
    release_data: Date;
    update_at: Date;
    symbol_url: string;
    logo_url: string;
}


export type Card = {
    id: string;
    name: string;
    supertype: string;
    subtypes: string;
    types: string;
    set: string;
    number: string;
    rarity: string;
}