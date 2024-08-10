import random


class Gene:
    def __init__(self, value):
        if value not in (0, 1):
            raise ValueError(f"Wrong Gene value: {value}")
        self.value = value

    def mutate(self):
        self.value = abs(self.value-1)


class Chromosome:
    def __init__(self):
        self.genes = [Gene(random.randint(0, 1)) for i in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() <= 0.5:
                gene.mutate()


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() <= 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        for chromosome in self.chromosomes:
            for gene in chromosome.genes:
                if gene.value != 1:
                    return False


class Organism:
    def __init__(self, dna, environment=0.5):
        self.dna = DNA()
        self.environment = float(environment)

    def mutate(self):
        print(self.environment)
        if random.random() <= self.environment:
            self.dna.mutate()

    def is_all_ones(self):
        return self.dna.is_all_ones()


# def find_DNA(environment=0.5):
#     generation = 0
#     limit = 100000000
#     organisms = [Organism(DNA(), environment) for _ in range(2)]
#     while True:
#         for organism in organisms:
#             organism.mutate()
#         if organism.dna.is_all_ones():
#             return generation
#         generation += 1
#         if generation >= limit:
#             return -1


# find_DNA()

new_organism = Organism(DNA())
x = 0
genes_list = []
for i in range(10):
    new_organism.mutate()
    x += 1
    for i in new_organism.dna.chromosomes:
        for y in i.genes:
            genes_list.append(y.value)
            print(genes_list)
        if 0 not in genes_list:
            print("Success")
            break
