from metaflow import FlowSpec, step, schedule, pypi_base
import numpy as np
import os
from metaflow import FlowSpec, step, batch, environment, IncludeFile


TOTAL_VECTORS = 1000
EMBEDDING_SIZE = 10



#@schedule(hourly=True)
@pypi_base(
    python="3.9.10",
    packages={
        'omnivector': '0.1.1',
        'numpy': '1.21.2',
    }
)
class Index(FlowSpec):

    @step
    def start(self):
        self.next(self.update_index_sim)

    @environment(vars={
        "OMNIVECTOR_CONFIG": './config.yml'})
    @step
    def update_index_sim(self):

        import numpy as np
        from omnivector.lancedb import LanceDB

        self.n_vectors =  np.random.randn(TOTAL_VECTORS, EMBEDDING_SIZE)

        # normalize the vectors to have unit length using numpy
        self.n_vectors = self.n_vectors/np.linalg.norm(self.n_vectors, axis=1, keepdims=True)
        ids = list(range(TOTAL_VECTORS))

        self.db = LanceDB()

        self.db.create_index(ids, self.n_vectors)

        self.next(self.search_sim)

    @step
    def search_sim(self):
        query = np.random.randn(1, EMBEDDING_SIZE)[0]
        query = query/np.linalg.norm(query)

        self.db.vector_search(query, k=1)

        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    Index()