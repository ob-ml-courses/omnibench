from metaflow import FlowSpec, step, schedule, pypi_base

TOTAL_VECTORS = 100000

@schedule(hourly=True)
@pypi_base(
    python="3.9.10",
    packages={
        'omnivector': '0.1.1',
        'numpy': '1.21.2'
    }
)
class Index(FlowSpec):

    @step
    def start(self):
        self.next(self.update_index_sim, self.search_sim)

    @step
    def update_index_sim(self):

        import numpy as np
        import omnivector as ov

        self.n_vectors = int(
            np.random.choice([.1, .2, .4]) * TOTAL_VECTORS
        )

        # do update

        self.next(self.join)

    @step
    def search_sim(self):
        self.next(self.join)

    @step
    def join(self, inputs):
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    Index()