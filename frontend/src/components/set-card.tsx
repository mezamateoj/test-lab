import { Set } from "@/app/lib/definitions";
import Image from "next/image"
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import Link from "next/link";
import { Button } from "./ui/button";

interface SetCardProps {
  set: Set;
}

export function SetCard({ set }: SetCardProps) {
  return (
    <Card className="h-full flex flex-col">
      <CardHeader>
        <CardTitle className="flex items-center justify-between">
          <span>{set.name}</span>
          <Image 
            src={set.symbol_url} 
            alt={`${set.name} symbol`} 
            width={30} 
            height={30}
          />
        </CardTitle>
      </CardHeader>
      <CardContent className="flex-grow">
        <Image 
          src={set.logo_url} 
          alt={`${set.name} logo`} 
          width={200} 
          height={100} 
          className="mb-4"
        />
        <p><strong>Set Id:</strong> {set.id}</p>
        <p><strong>Series:</strong> {set.series}</p>
        <p><strong>Total Cards:</strong> {set.total} ({set.printed_total} printed)</p>
        <div className="mt-4">

        <Link 
          href={`/sets/cards/${set.id}`}
          className="bg-primary text-primary-foreground shadow hover:bg-primary/90 p-2 rounded-md"
          >
            See cards
            </Link>
            </div>
      </CardContent>
    </Card>
  )
}

