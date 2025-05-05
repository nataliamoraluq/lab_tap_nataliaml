#MODELO DE DESCUENTO POR VOLUMENES VERS. CONSOLA BASE
#NATALIA ML. - TAP
#ok so, para no enrredarme, nombres re especificos, separados por _ y vamos por partess/ segmentos
# nombreDef once i get it and works
# var_name_meaning while i get it
from math import *

import math
import tkinter as tk
"""
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ------------------ ***  ENUNCIADO:  *** ----------------------------
La Espiga Dorada C.A. busca optimizar la gestión de inventario de sus sacos de harina de trigo. 
Han implementado una política de descuentos por volumen para incentivar a las panaderías a realizar 
pedidos más grandes. Sin embargo, reconocen que almacenar grandes cantidades también implica mayores costos. 
Además, la preparación de pedidos de diferentes tamaños conlleva costos operativos distintos. 

La gerente de operaciones de La Espiga Dorada C.A. necesita analizar los costos asociados a 
diferentes tamaños de pedido para una panadería cliente que tiene una demanda mensual constante de 40 sacos de harina de trigo HT-50. 
El costo por saco de harina es de $25.

·       ¿Cuál sería el costo total incluyendo el costo de la harina, el almacenamiento de un mes 
y la preparación del pedido si la panadería realiza un pedido de 10 sacos?

·       ¿Cuál sería el costo total si la panadería realiza un pedido de 45 sacos?

·       ¿Cómo debería la Espiga Dorada C.A. aconsejar a esta panadería para que gestione 
sus pedidos mensuales de 40 sacos de la manera más económica posible, considerando las opciones 
de realizar un solo pedido o varios pedidos más pequeños a lo largo del mes?


"""

def calcularCostoTotal_Descuento(demanda_anual, costo_unitario_base, rangos_descuento, costo_almacenamiento_mes, costo_pedido):
    #arr
    #
    resultados_costos = []
    cantidad_optima = 0 #
    costo_total_minimo = float('inf') #
    #
    #
    for rango in rangos_descuento:
        limite_inferior = rango['limite_inferior']
        descuento = rango['descuento'] / 100
        costo_almacenamiento_mensual = rango['costo_almacenamiento']
        costo_preparacion_pedido = rango['costo_pedido']

        #
        costo_unitario_con_descuento = costo_unitario_base * (1 - descuento)
        costo_mantenimiento_anual_unitario = costo_almacenamiento_mensual * 12  # Asumiendo porc. implícito del 100%
        #
        try:
            # Calcular Yi 
            yi = math.sqrt((2 * costo_preparacion_pedido * demanda_anual) / costo_mantenimiento_anual_unitario)

            # Ajustar Yi al rango
            cantidad_pedido = 0
            if yi >= limite_inferior and (rango.get('limite_superior') is None or yi < rango['limite_superior']):
                cantidad_pedido = yi #
            else:
                cantidad_pedido = limite_inferior #

            # Calcular el costo total anual para esta cantidad de pedido
            costo_adquisicion = costo_unitario_con_descuento * demanda_anual
            costo_pedido_anual = (demanda_anual / cantidad_pedido) * costo_preparacion_pedido
            costo_mantenimiento_anual = (cantidad_pedido / 2) * costo_mantenimiento_anual_unitario
            costo_total = costo_adquisicion + costo_pedido_anual + costo_mantenimiento_anual

            #resultados
            resultados_costos.append({
                'rango': f"{limite_inferior} - {rango.get('limite_superior', 'más')}",
                'cantidad_pedido': cantidad_pedido,
                'costo_unitario': costo_unitario_con_descuento,
                'costo_total': costo_total
            })

            if costo_total < costo_total_minimo: #si el costo t< q el min
                costo_total_minimo = costo_total
                cantidad_optima = cantidad_pedido

            #considerando el límite inferior del rango q sigue para asegurar elegir del dscto
            if rango.get('limite_superior') is not None: #OJO no puede ser NONE
                cantidad_pedido_limite = rango['limite_superior']
                costo_unitario_limite = costo_unitario_base * (1 - descuento)
                costo_mantenimiento_anual_limite = costo_almacenamiento_mensual * 12
                costo_adquisicion_limite = costo_unitario_limite * demanda_anual
                costo_pedido_anual_limite = (demanda_anual / cantidad_pedido_limite) * costo_preparacion_pedido
                costo_mantenimiento_anual_limite_calc = (cantidad_pedido_limite / 2) * costo_mantenimiento_anual_limite
                costo_total_limite = costo_adquisicion_limite + costo_pedido_anual_limite + costo_mantenimiento_anual_limite_calc
                #
                #
                #append 
                resultados_costos.append({
                    'rango': f"Límite inferior del siguiente: {cantidad_pedido_limite}",
                    'cantidad_pedido': cantidad_pedido_limite,
                    'costo_unitario': costo_unitario_limite,
                    'costo_total': costo_total_limite
                })
                if costo_total_limite < costo_total_minimo:
                    costo_total_minimo = costo_total_limite
                    cantidad_optima = cantidad_pedido_limite
        #except if ----
        except ValueError as e:
            print(f"Error al calcular para el rango {limite_inferior}: {e}")
            continue #then continue so no explotara
        #
    #
    return {'cantidad_optima': round(cantidad_optima, 2), 'costo_total_minimo': round(costo_total_minimo, 2), 'detalles_costos': resultados_costos}
#
# ------------------- ==== MAIN ========== -------------------------------------
#
if __name__ == "__main__":
    demanda_mensual = 40  # sacos por mes
    demanda_anual = demanda_mensual * 12  # sacos por año
    costo_unitario_base = 25  # $ por saco

    rangos_matrizDesc = [
        {'limite_inferior': 1, 'limite_superior': 6, 'descuento': 0, 'costo_almacenamiento': 0.15, 'costo_pedido': 2.50},
        {'limite_inferior': 6, 'limite_superior': 16, 'descuento': 4, 'costo_almacenamiento': 0.20, 'costo_pedido': 3.25},
        {'limite_inferior': 16, 'limite_superior': 31, 'descuento': 8, 'costo_almacenamiento': 0.28, 'costo_pedido': 4.00},
        {'limite_inferior': 31, 'limite_superior': 51, 'descuento': 12, 'costo_almacenamiento': 0.35, 'costo_pedido': 5.50},
        {'limite_inferior': 51, 'descuento': 16, 'costo_almacenamiento': 0.45, 'costo_pedido': 7.00},
    ]
    #
    #
    #
    resultados_optimizacion = calcularCostoTotal_Descuento(
        demanda_anual, costo_unitario_base, rangos_matrizDesc,
        rangos_matrizDesc[0]['costo_almacenamiento'], rangos_matrizDesc[0]['costo_pedido']
    )
    # salida del analisis, resultados y recomendaciones *SELF QUOTE: once i get the window all done, o imprimimos en textarea o 
    #imprimos una parte y las recomendaciones las dejames para el informe
    #whatever works best por tema tiempo
    print(" ------------------ LA ESPIGA DORADA C.A. ---------------------")
    print(f"\n")
    #first/ main ------------------ ANALISIS -----------------------
    print(" *** --- Análisis del Modelo De Descuento por Volumen --- ***")
    print(f"Demanda Anual: {demanda_anual} sacos")
    print(f"Costo Unitario Base: ${costo_unitario_base:.2f}")
    #
    print("\n--- Resultados por Rango de Pedido ---")
    for resultado in resultados_optimizacion['detalles_costos']:
        print(f"Rango: {resultado['rango']}")
        print(f"  Cantidad de Pedido: {resultado['cantidad_pedido']:.2f} sacos")
        print(f"  Costo Unitario: ${resultado['costo_unitario']:.2f}")
        print(f"  Costo Total Anual: ${resultado['costo_total']:.2f}")
        print("-" * 30)
    # ------------------- RECOMENDACIONES --------------------------------
    print("\n--- Recomendación Óptima ---")
    print(f"Cantidad Óptima de Pedido Anual: {resultados_optimizacion['cantidad_optima']} sacos")
    print(f"Costo Total Anual Mínimo: ${resultados_optimizacion['costo_total_minimo']:.2f}")
    #-----------------------------------------------------------------------------------------------------------------------
    # REQUISITOS DEL CASO
    print("\n--- Respuestas a las preguntas de los requisitos - Espiga Dorada CA ---")
    #

    # Pregunta 1: Costo total por pedido de 10 sacos
    costo_total_10_sacos = 0
    costo_unitario_10_sacos = 0
    costo_pedido_10_sacos = 0
    costo_almacenamiento_10_sacos_mes = 0
    #
    # leyendo la matriz
    for rango in rangos_matrizDesc:
        if 6 <= 10 < rango.get('limite_superior', float('inf')):
            costo_unitario_10_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_10_sacos = rango['costo_pedido']
            costo_almacenamiento_10_sacos_mes = rango['costo_almacenamiento']
            costo_total_10_sacos = (10 * costo_unitario_10_sacos) + costo_pedido_10_sacos + (10 * costo_almacenamiento_10_sacos_mes)
            break
        elif 1 <= 10 < 6:
            costo_unitario_10_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_10_sacos = rango['costo_pedido']
            costo_almacenamiento_10_sacos_mes = rango['costo_almacenamiento']
            costo_total_10_sacos = (10 * costo_unitario_10_sacos) + costo_pedido_10_sacos + (10 * costo_almacenamiento_10_sacos_mes)
            break
    #
    print(f"\nCosto total por pedido de 10 sacos (mensual): ${costo_total_10_sacos:.2f}")
    #
    # Pregunta 2: Costo total por pedido de 45 sacos
    costo_total_45_sacos = 0
    costo_unitario_45_sacos = 0
    costo_pedido_45_sacos = 0
    costo_almacenamiento_45_sacos_mes = 0
    #
    for rango in rangos_matrizDesc:
        if 31 <= 45 < rango.get('limite_superior', float('inf')):
            costo_unitario_45_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_45_sacos = rango['costo_pedido']
            costo_almacenamiento_45_sacos_mes = rango['costo_almacenamiento']
            costo_total_45_sacos = (45 * costo_unitario_45_sacos) + costo_pedido_45_sacos + (45 * costo_almacenamiento_45_sacos_mes)
            break
        elif 1 <= 45 < 6:
            costo_unitario_45_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_45_sacos = rango['costo_pedido']
            costo_almacenamiento_45_sacos_mes = rango['costo_almacenamiento']
            costo_total_45_sacos = (45 * costo_unitario_45_sacos) + costo_pedido_45_sacos + (45 * costo_almacenamiento_45_sacos_mes)
            break
        elif 6 <= 45 < 16:
            costo_unitario_45_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_45_sacos = rango['costo_pedido']
            costo_almacenamiento_45_sacos_mes = rango['costo_almacenamiento']
            costo_total_45_sacos = (45 * costo_unitario_45_sacos) + costo_pedido_45_sacos + (45 * costo_almacenamiento_45_sacos_mes)
            break
        elif 16 <= 45 < 31:
            costo_unitario_45_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_45_sacos = rango['costo_pedido']
            costo_almacenamiento_45_sacos_mes = rango['costo_almacenamiento']
            costo_total_45_sacos = (45 * costo_unitario_45_sacos) + costo_pedido_45_sacos + (45 * costo_almacenamiento_45_sacos_mes)
            break
        elif 51 <= 45: # Esto nunca se cumplirá, pero es para el rango final
            costo_unitario_45_sacos = costo_unitario_base * (1 - rango['descuento'] / 100)
            costo_pedido_45_sacos = rango['costo_pedido']
            costo_almacenamiento_45_sacos_mes = rango['costo_almacenamiento']
            costo_total_45_sacos = (45 * costo_unitario_45_sacos) + costo_pedido_45_sacos + (45 * costo_almacenamiento_45_sacos_mes)
            break
    #-----------------------------------------------------------------------------------------------------------------------
    #
    #
    print(f"Costo total por pedido de 45 sacos (mensual): ${costo_total_45_sacos:.2f}")
    #-----------------------------------------------------------------------------------------------------------------------
    # Pregunta 3: Recomendación para la panadería
    print("\n--- Recomendación para la Panadería ---")
    print("La panadería tiene una demanda mensual constante de 40 sacos.")
    print("Analizando los costos totales anuales bajo diferentes políticas de pedido:")
    for resultado in resultados_optimizacion['detalles_costos']:
        print(f"- Pedir {round(resultado['cantidad_pedido'] / 12, 2)} veces al mes ({resultado['cantidad_pedido']:.2f} anual): Costo Total Anual = ${resultado['costo_total']:.2f}")
    #-----------------------------------------------------------------------------------------------------------------------
    cantidad_optima_mensual = resultados_optimizacion['cantidad_optima'] / 12
    costo_total_minimo_mensual = resultados_optimizacion['costo_total_minimo'] / 12
    #-----------------------------------------------------------------------------------------------------------------------
    print(f"\nLa estrategia más económica para la panadería, considerando los descuentos por volumen y los costos asociados, sería realizar pedidos de aproximadamente {round(cantidad_optima_mensual, 2)} sacos de harina cada {round(12 / (resultados_optimizacion['cantidad_optima'] / 40), 2)} meses, con un costo total anual estimado de ${resultados_optimizacion['costo_total_minimo']:.2f} (o ${costo_total_minimo_mensual:.2f} mensual).")
    print("Es importante que la panadería evalúe la viabilidad de almacenar las cantidades recomendadas y la frecuencia de sus necesidades operativas.")
    print("Considerando la demanda mensual de 40 sacos, analizar los costos para pedidos que se acerquen a este valor o múltiplos del mismo dentro de los rangos de descuento podría ser beneficioso.")
    #-----------------------------------------------------------------------------------------------------------------------
    # anlisis extra/adicio para la pregunta 3 considerando la demanda mensual!
    print("\n--- Análisis Adicional para Demanda Mensual de 40 Sacos ---")
    costos_mensuales_analisis = []
    for rango in rangos_matrizDesc:
        limite_inferior = rango['limite_inferior']
        descuento = rango['descuento'] / 100
        costo_almacenamiento_mensual = rango['costo_almacenamiento']
        costo_preparacion_pedido = rango['costo_pedido']
        costo_unitario_con_descuento = costo_unitario_base * (1 - descuento)
        # Costo de pedir 40 sacos (un pedido al mes)
        if limite_inferior <= 40 < rango.get('limite_superior', float('inf')):
            costo_mensual_40 = (40 * costo_unitario_con_descuento) + costo_preparacion_pedido + (40 * costo_almacenamiento_mensual)
            costos_mensuales_analisis.append({'cantidad': 40, 'costo': round(costo_mensual_40, 2),})
                                               # Para widgets más modernos
    #-----------------------------------------------------------------------------------------------------------------------
#
# VISTA MAS SENCILLA (IF SO, PROBAR SI EL TIEMPO NOS ALCANZA ONCE ALL THIS WORKS)
#

"""
def showCalcs():
    try:
        D = float(entry_demanda.get())
        costoBase = float(entry_costo_base.get())
        porcRetencion = float(entry_retencion.get()) / 100
        # obteniendo los datos de la matriz de rangos

        resultados = calcularCostoTotal_Descuento(D, costoBase, rangos, porcRetencion)

        txtResultados.delete("1.0", tk.END)
        txtResultados.insert(tk.END, "--- Resultados del Análisis ---\n")
        txtResultados.insert(tk.END, f"Cantidad Óptima: {resultados['cantidad_optima']}\n")
        txtResultados.insert(tk.END, f"Costo Total Mínimo: {resultados['costo_total_minimo']}\n\n")
        txtResultados.insert(tk.END, "--- Costos por Rango ---\n")
        for detalle in resultados['detalles_costos']:
            txtResultados.insert(tk.END, f"Rango: {detalle['rango']}\n")
            txtResultados.insert(tk.END, f"  Cantidad: {detalle['cantidad_pedido']:.2f}\n")
            txtResultados.insert(tk.END, f"  Costo Unitario: ${detalle['costo_unitario']:.2f}\n")
            txtResultados.insert(tk.END, f"  Costo Total Anual: ${detalle['costo_total']:.2f}\n")
            txtResultados.insert(tk.END, "-------------------------\n")

        # (Opcional) para la gráfica usar matplotlib y FigureCanvasTkAgg

    except ValueError:
        txtResultados.delete("1.0", tk.END)
        txtResultados.insert(tk.END, "Error: Por favor, ingrese valores numéricos válidos.\n")
"""
# VENTANITA EN TKINTER
"""
btnCalcular = tk.Button(window, text="Calcular EOQ con Descuento", command=showCalcs())
btnCalcular.pack(pady=10)
txtResultados = tk.Text(window, height=15, width=60)
txtResultados.pack(padx=10, pady=10)
# (agg la gráfica here)"""