import v3io
import v3io.dataplane
import os

class DistributedCounter:
    def __init__(self, container='bigdata', table_path='/my_counters/', counter_key='distributed_counter'):
        self.client = v3io.dataplane.Client(endpoint=os.getenv('V3IO_API', 'http://v3io-webapi:8081'))
        self.container = container
        self.table_path = table_path
        self.counter_key = counter_key
        self._initialize_counter()

    def _initialize_counter(self):
        # Ensure the counter is initialized
        response = self.client.kv.get(container=self.container, table_path=self.table_path, key=self.counter_key)
        if response.status_code == 404:
            self.client.kv.put(container=self.container, table_path=self.table_path, key=self.counter_key, attributes={'counter': 0})

    def get_unique_number(self):
        # Atomically increment the counter and return the new value
        response = self.client.kv.update(container=self.container, table_path=self.table_path, key=self.counter_key, expression="counter = counter + 1", return_attributes=["counter"])
        return response.output.item['counter']

if __name__ == "__main__":
    # Initialize the distributed counter
    counter = DistributedCounter()

    # Get a unique number
    unique_number = counter.get_unique_number()
    print(f"Unique Number: {unique_number}")
