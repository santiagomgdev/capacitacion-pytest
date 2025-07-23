def filtrar_clientes_activos(clientes: list[dict]) -> list[dict]:
    clientes_activos = []
    for cliente in clientes:
        if cliente.get("activo", False) is True:
            clientes_activos.append(cliente)
    return clientes_activos