from services.data_factory import crear_datos_demo


def test_reglas_negocio_basicas() -> None:
    repo = crear_datos_demo()
    trabajadores = repo.listar_trabajadores()

    assert len(trabajadores) == 41
    assert any("Gerente" in t.get_puesto() for t in trabajadores)
    assert sum(1 for t in trabajadores if t.get_puesto() == "Jefe de Área") == 5

    validaciones = repo.validar_reglas_de_negocio()
    assert all(item["cumple"] for item in validaciones)


def test_tecnico_incluye_experiencia_en_resumen() -> None:
    repo = crear_datos_demo()
    tecnico = next(t for t in repo.listar_trabajadores() if t.get_puesto() == "Personal Técnico")
    assert "Experiencia" in tecnico.get_resumen()


def test_gerente_no_tiene_jefe() -> None:
    repo = crear_datos_demo()
    gerente = next(t for t in repo.listar_trabajadores() if t.get_puesto() == "Gerente General")
    assert gerente.get_jefe_inmediato() == "No tiene jefe inmediato"
