'''Assignment 6: Custom Database Record Simulator'''
class RecordNotFoundError:pass

class DatabaseRecord:
    def __init__(self,record_id:int,kwargs:dict):
        self.record_id=record_id
        self.data=kwargs

    def __repr__(self):
        return f"Record(id={self.record_id}, data={self.data})"

    def __str__(self):
        return f"Record(id={self.record_id}, data={self.data})"

class ResultSetIterator:
    def __init__(self,records_list:list):
        self.records_list=records_list
        self.index_counter=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_counter >= len(self.records_list):
            raise StopIteration
        record = self.records_list[self.index_counter]
        self.index_counter += 1
        return record

class DatabaseResultSet:
    def __init__(self,records_list:list):
        self.records_list=records_list

    def __len__(self):
        return len(self.records_list)

    def __iter__(self):
        return ResultSetIterator(self.records_list)

    def __getitem__(self, key):
        if type(key) is int:
            if key >= len(self.records_list):
                raise IndexError
            return self.records_list[key]
        else:
            for obj in self.records_list:
                if key==obj.data["name"]:
                    return obj
            raise RecordNotFoundError(f"Record with name {key!r} not found in database.")

def main():
    # Setup records
    r1 = DatabaseRecord(101, {"name": "Alice", "role": "Admin"})
    r2 = DatabaseRecord(102, {"name": "Bob", "role": "User"})

    results = DatabaseResultSet([r1, r2])

    # 1. Length
    print(len(results))  # Output: 2

    # 2. Integer Indexing
    print(results[0].data["role"])  # Output: Admin

    # 3. String lookup
    record = results["Bob"]
    print(record.record_id)  # Output: 102

    # 4. Iteration
    for rec in results:
        print(rec.record_id)
    # Output:
    # 101
    # 102

    # 5. Missing key lookup
    try:
        missing = results["Charlie"]
    except RecordNotFoundError as e:
        print(e)  # Output: Record with name 'Charlie' not found in database.

if __name__ == "__main__":  main()

