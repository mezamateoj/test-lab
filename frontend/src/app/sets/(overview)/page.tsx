import Sets from '@/components/all-sets'
import { Skeleton } from '@/components/ui/skeleton'
import React, { Suspense } from 'react'

export default async function page() {

  return (

    <div>
      <Suspense fallback={<Skeleton className="h-[125px] w-[250px] rounded-xl" />}>
          <Sets />
      </Suspense>
    </div>

  )
}
