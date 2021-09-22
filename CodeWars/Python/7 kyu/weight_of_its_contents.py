def content_weight(bottle_weight, scale):
    scale, _, keyword = scale.split()

    if keyword == 'larger':
        return bottle_weight - (bottle_weight / (int(scale) + 1))

    return bottle_weight / (int(scale) + 1)