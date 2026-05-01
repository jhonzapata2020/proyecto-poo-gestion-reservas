"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación

Para ejecutar:
    python software_fj_unico.py
"""
from abc import ABC, abstractmethod
from datetime import datetime

# ============================================================
# #Estructura base del sistema, clases abstractas, clientes,
# servicios, reservas y listas internas.
# ============================================================


class EntidadSistema(ABC):
    """
    Clase abstracta base para entidades generales del sistema.
    Demuestra abstracción.
    """

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(EntidadSistema):
    """
    Clase Cliente con encapsulación y validaciones básicas.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def mostrar_info(self):
        return (
            f"Cliente #{self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )


class Servicio(EntidadSistema):
    """
    Clase abstracta para servicios.
    Las clases hijas implementan cálculo de costo.
    Demuestra abstracción y polimorfismo.
    """

    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)
        self._nombre = nombre
        self._tarifa_base = tarifa_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion_horas):
        pass

    def mostrar_info(self):
        return (
            f"Servicio #{self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Tarifa base: ${self.tarifa_base}"
        )


class ReservaSala(Servicio):
    """
    Servicio especializado para reserva de salas.
    """

    def __init__(self, identificador, nombre, tarifa_base, capacidad):
        super().__init__(identificador, nombre, tarifa_base)
        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    def calcular_costo(self, duracion_horas):
        recargo_capacidad = 20000 if self.capacidad > 20 else 0
        return self.tarifa_base * duracion_horas + recargo_capacidad

    def mostrar_info(self):
        return super().mostrar_info() + f" | Capacidad: {self.capacidad} personas"


class AlquilerEquipo(Servicio):
    """
    Servicio especializado para alquiler de equipos.
    """

    def __init__(self, identificador, nombre, tarifa_base, tipo_equipo):
        super().__init__(identificador, nombre, tarifa_base)
        self._tipo_equipo = tipo_equipo

    @property
    def tipo_equipo(self):
        return self._tipo_equipo

    def calcular_costo(self, duracion_horas):
        seguro = 15000
        return self.tarifa_base * duracion_horas + seguro

    def mostrar_info(self):
        return super().mostrar_info() + f" | Equipo: {self.tipo_equipo}"


class AsesoriaEspecializada(Servicio):
    """
    Servicio especializado para asesorías.
    """

    def __init__(self, identificador, nombre, tarifa_base, area):
        super().__init__(identificador, nombre, tarifa_base)
        self._area = area

    @property
    def area(self):
        return self._area

    def calcular_costo(self, duracion_horas):
        recargo_especialista = 30000
        return self.tarifa_base * duracion_horas + recargo_especialista

    def mostrar_info(self):
        return super().mostrar_info() + f" | Área: {self.area}"


class Reserva:
    """
    Clase que integra cliente, servicio, duración y estado.
    """

    ESTADOS_VALIDOS = ["pendiente", "confirmada", "cancelada"]

    def __init__(self, identificador, cliente, servicio, duracion_horas):
        self._identificador = identificador
        self._cliente = cliente
        self._servicio = servicio
        self._duracion_horas = duracion_horas
        self._estado = "pendiente"
        self._fecha_creacion = datetime.now()

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion_horas(self):
        return self._duracion_horas

    @property
    def estado(self):
        return self._estado

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    def confirmar(self):
        self._estado = "confirmada"

    def cancelar(self):
        self._estado = "cancelada"

    def calcular_total(self):
        return self.servicio.calcular_costo(self.duracion_horas)

    def mostrar_info(self):
        return (
            f"Reserva #{self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion_horas} hora(s) | "
            f"Estado: {self.estado} | "
            f"Total: ${self.calcular_total():,.0f}"
        )


class SistemaGestion:
    """
    Clase principal que maneja listas internas.
    No utiliza bases de datos.
    """

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def buscar_cliente(self, identificador):
        for cliente in self.clientes:
            if cliente.identificador == identificador:
                return cliente
        return None

    def buscar_servicio(self, identificador):
        for servicio in self.servicios:
            if servicio.identificador == identificador:
                return servicio
        return None

    def buscar_reserva(self, identificador):
        for reserva in self.reservas:
            if reserva.identificador == identificador:
                return reserva
        return None

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_info())

    def listar_servicios(self):
        for servicio in self.servicios:
            print(servicio.mostrar_info())

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_info())

