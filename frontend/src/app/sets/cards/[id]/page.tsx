import { fetchSetById } from '@/app/lib/data';
import { notFound } from 'next/navigation';
 
export default async function Page(props: {params: Promise<{id: string}>}) {
  const params = await props.params
  const id = params.id

  const data = await fetchSetById(id);
    
  if (!data) {
    notFound()
  }

  
  return (
    <main>
        <pre>
            {JSON.stringify(data)}
        </pre>
    </main>
  );
}