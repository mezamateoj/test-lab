import { Set } from "@/app/lib/definitions";
import { SetCard } from "./set-card";

interface SetGridProps {
  sets: Set[];
}

export function SetGrid({ sets }: SetGridProps) {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {sets.map((set) => (
          <SetCard key={set.id} set={set} />
        ))}
      </div>
    </div>
  )
}

