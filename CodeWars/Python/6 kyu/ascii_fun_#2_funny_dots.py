def dot(width, height):
    head = f'+{"---+" * width}\n'
    body = f'{head}'.join(f'|{" o |" * width}\n' for _ in range(height))
    return head + body + head.strip('\n')


print(dot(3, 2))