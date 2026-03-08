import os
import asyncio
import random
SOURCE_KEYS = [
    os.getenv("SOURCE1_KEY"),
    os.getenv("SOURCE2_KEY"),
    os.getenv("SOURCE3_KEY")
]

async def fetch_data(source_id, key):
    
    print(f"Fetching data from source {source_id} with key {key}...")
    await asyncio.sleep(random.uniform(1, 3))
    data = {
        "source": source_id,
        "records": [random.randint(1, 100) for _ in range(5)]
    }
    print(f"Fetched data from source {source_id}: {data['records']}")
    return data

async def main():
    tasks = [fetch_data(i+1, key) for i, key in enumerate(SOURCE_KEYS)]
    results = await asyncio.gather(*tasks)
    combined_records = []
    for r in results:
        combined_records.extend(r["records"])
    summary = {
        "total_sources": len(results),
        "total_records": len(combined_records),
        "average_value": sum(combined_records)/len(combined_records),
        "all_records": combined_records
    }
    
    print("\n=== Combined Summary ===")
    for k, v in summary.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    asyncio.run(main())