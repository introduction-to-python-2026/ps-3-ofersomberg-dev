def approximate_pi(n_terms):
    lebianese = []
    for i in range(n_terms):
        thing = ((-1) ** i) / (2 * i + 1)
        lebianese.append(thing)
    return (sum(lebianese)*4)
