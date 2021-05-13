from math import e, factorial

def poisson_pmf(lam, k):
    return (e ** (-lam) * lam**k) / factorial(k)

# print(poisson_pmf(10, 10))


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)



lam = 10
k = 10


# for n in range(k, 10000):
#     print(f'binom: {round(binomial_pmf(n, k, p=(lam/n)), 7)}')
#     print(f'poiss: {round(poisson_pmf(lam, k), 7)}')
#     print()

# lam = 15 * (15/10)
# k = 20
# print(lam)
# print(poisson_pmf(lam, k))


def poisson_cdf(lam, low_k, high_k):
    proba = 0
    for k in range(low_k, high_k+1):
        proba += poisson_pmf(lam, k)
    return proba

# lam = 15*(15/10)
# print(1 - poisson_cdf(lam, low_k=0, high_k=22))





def poisson_pmf_dict(lam, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lam, k)

    return d

# d = poisson_pmf_dict(lam=10, low_k=0, high_k=30)

# for k, p in d.items():
#     print(f'{k}: {p}')


def poisson_count_exp(lam, low_k, high_k, num_samples=10000):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = round(poisson_pmf(lam, k) * num_samples)

    return d

d = poisson_count_exp(lam=10, low_k=5, high_k=15, num_samples=10000)

for k, cnt in d.items():
    print(f'{k}: {cnt}')
