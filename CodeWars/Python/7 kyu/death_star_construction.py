def death_star(week, attack):
    delivered_materials = week[:attack]
    iron = 100 - sum(el[0] for el in delivered_materials)
    steel = 75 - sum(el[1] for el in delivered_materials)
    chromium = 50 - sum(el[2] for el in delivered_materials)

    if iron > 0 or steel > 0 or chromium > 0:
        return f"The station is destroyed! \
It needed {iron if iron > 0 else 0} \
iron, {steel if steel > 0 else 0} steel and \
{chromium if chromium > 0 else 0} chromium for completion."

    return "The station is completed!"