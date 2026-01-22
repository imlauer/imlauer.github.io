---
title: "Gambling"
date: 2025-12-29T12:14:54-03:00
draft: true
---
En este stream Reckful enseña un poco de "gambling" invertir: [https://youtube.com/watch?v=2NnNKzrNPBs](https://youtube.com/watch?v=2NnNKzrNPBs)

# Gentileza de Claude.

# Guía Completa de Opciones Financieras y Script de Trading

Voy a explicarte desde cero cómo funcionan las opciones y luego te daré un script completo para ayudarte a analizar oportunidades. Tómate tu tiempo para leer, esto es importante.

## 📚 Parte 1: ¿Qué son las opciones?

### Concepto básico
Imagina que ves una casa que te gusta y cuesta $100,000, pero no tenés el dinero ahora. Le pagás $2,000 al dueño por el **derecho** (no la obligación) de comprarla a $100,000 en 3 meses. 

**Escenario A:** En 3 meses la casa vale $120,000 → Ejercés tu derecho, la comprás a $100,000 y ganás $18,000 (menos los $2,000 que pagaste)

**Escenario B:** En 3 meses la casa vale $80,000 → No ejercés el derecho. Solo perdés los $2,000 iniciales.

### Tipos de opciones

**CALL (Opción de Compra)**
- Te da el derecho de **comprar** una acción a un precio fijo
- Apostás a que el precio **SUBA**
- Ejemplo: Apple está a $230, comprás un CALL de $240
  - Si Apple llega a $260, ganás (260-240) × 100 = $2,000 por contrato
  - Si queda en $230, perdés lo que pagaste por el CALL

**PUT (Opción de Venta)**
- Te da el derecho de **vender** una acción a un precio fijo
- Apostás a que el precio **BAJE**
- Ejemplo: Intel está a $49, comprás un PUT de $48
  - Si Intel cae a $40, ganás (48-40) × 100 = $800 por contrato
  - Si queda en $49, perdés lo que pagaste por el PUT

### Elementos clave

1. **Strike Price (Precio de Ejercicio):** El precio al que podés comprar/vender
2. **Expiration Date (Fecha de Vencimiento):** Cuándo expira tu derecho
3. **Premium (Prima):** Lo que pagás por la opción
4. **Contrato = 100 acciones:** Cada opción controla 100 acciones

### Ejemplo real del documento

En el texto, el streamer compró **Intel PUT de $48 a $0.34**:
- Pagó $34 por contrato ($0.34 × 100 acciones)
- Intel cerró en $45.80
- El PUT valía $2.17 al cierre (48 - 45.80)
- Ganancia: ($2.17 - $0.34) × 100 = **$183 por contrato (538% de retorno)**

## ⚠️ Advertencias CRÍTICAS

1. **Puedes perder el 100% de tu inversión** en opciones
2. **La volatilidad es extrema** - puedes ganar o perder 500% en horas
3. **El tiempo trabaja en tu contra** - las opciones pierden valor cada día
4. **NO uses dinero que no puedas perder**
5. **Las opciones son derivados complejos** - practica con simuladores primero

## 🐍 Script de Python para Análisis de Opciones## 📖 Cómo usar el script

### Instalación de dependencias
```bash
pip install yfinance pandas numpy matplotlib scipy
```

### Ejecución básica
```python
python script.py
```

El script te guiará con un menú interactivo.

## 🎓 Estrategias explicadas del documento

### 1. **Buying CALLs (Comprar opciones de compra)**
- Apostás a que el precio suba
- Riesgo limitado al costo del contrato
- Potencial de ganancia ilimitado (teóricamente)

### 2. **Buying PUTs (Comprar opciones de venta)**
- Apostás a que el precio baje
- Ejemplo del documento: Intel PUT funcionó perfecto
- Ganó 538% en horas porque predijo la caída

### 3. **Selling PUTs (Vender opciones de venta) - RIESGOSO**
- Lo que hizo con Apple al final del documento
- "Jugás de banquero" - cobras la prima
- Si el precio no baja mucho, te quedás con todo el dinero
- **PELIGRO:** Si baja mucho, tus pérdidas pueden ser enormes

### 4. **Hedging (Cobertura)**
- Comprás acciones + PUTs como seguro
- Si las acciones bajan, las PUTs suben
- Es como pagar un seguro contra caídas

## 💡 Consejos basados en el documento

1. **Volatilidad = Oportunidad**: Las primas son más caras en mercados volátiles, pero también hay más movimiento

2. **Timing es todo**: El streamer compró Intel PUTs cuando vio una subida del 15% que no parecía sostenible

3. **Expiraciones cortas = Más riesgo**: Él compraba opciones que expiraban el mismo día (0DTE - Zero Days To Expiration)

4. **Liquidez importa**: Siempre verificá volumen y open interest para poder salir de la posición

5. **No te enamores de la posición**: Si ves ganancias, considerá tomar profits. Él se arrepintió de no vender cuando Intel subió temporalmente

## ⚠️ Advertencias finales

El documento muestra a alguien ganando mucho dinero rápidamente, pero también menciona:

- Perdió $85,000 en un día en 2014 (GTAT)
- En poker, ganó mucho y después "perdió todo en un stream"
- Las opciones son extremadamente volátiles

**Mi consejo profesional:**
1. Usa simuladores por 3-6 meses antes de arriesgar dinero real
2. Empieza con montos que no te duelan perder ($100-500)
3. Estudia análisis técnico y fundamental
4. Lee libros como "Options as a Strategic Investment"
5. Considerá cursos de trading certificados

¿Querés que profundice en algún aspecto específico o que te explique alguna estrategia en particular?

```python
"""
Sistema Completo de Análisis y Trading de Opciones
Autor: Asistente AI
Versión: 1.0
ADVERTENCIA: Este script es educativo. Nunca inviertas dinero que no puedas perder.
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from scipy.stats import norm
import warnings
warnings.filterwarnings('ignore')

class OptionsAnalyzer:
    """Analizador completo de opciones financieras"""
    
    def __init__(self, ticker):
        """
        Inicializa el analizador con un ticker
        
        Args:
            ticker (str): Símbolo de la acción (ej: 'AAPL', 'MSFT')
        """
        self.ticker = ticker.upper()
        self.stock = yf.Ticker(self.ticker)
        self.current_price = None
        self.load_data()
    
    def load_data(self):
        """Carga datos actuales de la acción"""
        try:
            info = self.stock.info
            self.current_price = info.get('currentPrice') or info.get('regularMarketPrice')
            print(f"\n{'='*60}")
            print(f"📊 Análisis de {self.ticker}")
            print(f"{'='*60}")
            print(f"Precio actual: ${self.current_price:.2f}")
            print(f"Empresa: {info.get('longName', 'N/A')}")
            print(f"Sector: {info.get('sector', 'N/A')}")
        except Exception as e:
            print(f"Error cargando datos: {e}")
            self.current_price = None
    
    def get_options_chain(self, expiration_date=None):
        """
        Obtiene la cadena de opciones para una fecha
        
        Args:
            expiration_date (str): Fecha en formato 'YYYY-MM-DD' o None para la más cercana
        """
        try:
            if expiration_date is None:
                expirations = self.stock.options
                if not expirations:
                    print("No hay opciones disponibles para este ticker")
                    return None, None
                expiration_date = expirations[0]
                print(f"\nUsando fecha de expiración: {expiration_date}")
            
            opt = self.stock.option_chain(expiration_date)
            calls = opt.calls
            puts = opt.puts
            
            print(f"\n📞 CALLs disponibles: {len(calls)}")
            print(f"📉 PUTs disponibles: {len(puts)}")
            
            return calls, puts
        except Exception as e:
            print(f"Error obteniendo opciones: {e}")
            return None, None
    
    def analyze_option_opportunity(self, option_type='call', target_return=1.0, days_to_expiry=30):
        """
        Analiza oportunidades de trading de opciones
        
        Args:
            option_type (str): 'call' o 'put'
            target_return (float): Retorno objetivo (1.0 = 100%)
            days_to_expiry (int): Días máximos hasta expiración
        """
        if self.current_price is None:
            print("No se pudo obtener el precio actual")
            return None
        
        # Buscar fecha de expiración apropiada
        expirations = self.stock.options
        target_date = datetime.now() + timedelta(days=days_to_expiry)
        
        best_expiry = None
        for exp in expirations:
            exp_date = datetime.strptime(exp, '%Y-%m-%d')
            if exp_date <= target_date:
                best_expiry = exp
        
        if best_expiry is None:
            best_expiry = expirations[0] if expirations else None
        
        if best_expiry is None:
            print("No hay fechas de expiración disponibles")
            return None
        
        calls, puts = self.get_options_chain(best_expiry)
        
        if calls is None or puts is None:
            return None
        
        options = calls if option_type.lower() == 'call' else puts
        
        print(f"\n{'='*60}")
        print(f"🎯 Buscando {option_type.upper()}s con retorno objetivo: {target_return*100:.0f}%")
        print(f"{'='*60}")
        
        opportunities = []
        
        for idx, row in options.iterrows():
            strike = row['strike']
            premium = row['lastPrice']
            volume = row['volume']
            open_interest = row['openInterest']
            implied_vol = row.get('impliedVolatility', 0)
            
            if premium <= 0 or volume == 0:
                continue
            
            # Calcular precio objetivo para alcanzar el retorno
            if option_type.lower() == 'call':
                # Para CALL: necesitamos que el precio suba
                target_price = strike + premium * (1 + target_return)
                price_change_needed = ((target_price - self.current_price) / self.current_price) * 100
                breakeven = strike + premium
            else:
                # Para PUT: necesitamos que el precio baje
                target_price = strike - premium * (1 + target_return)
                price_change_needed = ((target_price - self.current_price) / self.current_price) * 100
                breakeven = strike - premium
            
            # Calcular probabilidad usando modelo simplificado
            probability = self.estimate_probability(target_price, best_expiry, implied_vol)
            
            # Calcular score de oportunidad
            score = self.calculate_opportunity_score(
                premium, volume, open_interest, probability, price_change_needed
            )
            
            opportunities.append({
                'strike': strike,
                'premium': premium,
                'cost_per_contract': premium * 100,
                'volume': volume,
                'open_interest': open_interest,
                'implied_volatility': implied_vol * 100,
                'target_price': target_price,
                'breakeven': breakeven,
                'price_change_needed': price_change_needed,
                'probability': probability * 100,
                'potential_profit': premium * 100 * target_return,
                'score': score
            })
        
        if not opportunities:
            print("No se encontraron oportunidades")
            return None
        
        # Ordenar por score
        df_opps = pd.DataFrame(opportunities)
        df_opps = df_opps.sort_values('score', ascending=False)
        
        # Mostrar top 5
        print("\n🏆 TOP 5 OPORTUNIDADES:\n")
        for i, row in df_opps.head(5).iterrows():
            print(f"\n#{i+1} - Strike ${row['strike']:.2f}")
            print(f"   💰 Prima: ${row['premium']:.2f} (Costo: ${row['cost_per_contract']:.0f} por contrato)")
            print(f"   🎯 Precio objetivo: ${row['target_price']:.2f}")
            print(f"   📊 Breakeven: ${row['breakeven']:.2f}")
            print(f"   📈 Cambio necesario: {row['price_change_needed']:+.2f}%")
            print(f"   🎲 Probabilidad estimada: {row['probability']:.1f}%")
            print(f"   💵 Ganancia potencial: ${row['potential_profit']:.0f}")
            print(f"   📊 Volumen: {int(row['volume'])} | Open Interest: {int(row['open_interest'])}")
            print(f"   ⚡ Volatilidad implícita: {row['implied_volatility']:.1f}%")
            print(f"   ⭐ Score: {row['score']:.2f}/100")
        
        return df_opps
    
    def estimate_probability(self, target_price, expiration_date, implied_vol):
        """
        Estima probabilidad de alcanzar precio objetivo usando Black-Scholes simplificado
        
        Args:
            target_price (float): Precio objetivo
            expiration_date (str): Fecha de expiración
            implied_vol (float): Volatilidad implícita
        """
        if self.current_price is None or implied_vol == 0:
            return 0.5
        
        try:
            days_to_expiry = (datetime.strptime(expiration_date, '%Y-%m-%d') - datetime.now()).days
            if days_to_expiry <= 0:
                return 0
            
            time_to_expiry = days_to_expiry / 365.0
            
            # Cálculo simplificado usando distribución normal
            log_return = np.log(target_price / self.current_price)
            volatility = implied_vol * np.sqrt(time_to_expiry)
            
            if volatility == 0:
                return 0.5
            
            z_score = log_return / volatility
            probability = norm.cdf(z_score)
            
            return max(0.01, min(0.99, probability))
        except:
            return 0.5
    
    def calculate_opportunity_score(self, premium, volume, open_interest, probability, price_change):
        """
        Calcula un score de 0-100 para la oportunidad
        
        Factores:
        - Liquidez (volumen y open interest)
        - Probabilidad de éxito
        - Relación riesgo/recompensa
        - Realismo del movimiento de precio necesario
        """
        # Score de liquidez (0-30 puntos)
        liquidity_score = min(30, (volume / 100) + (open_interest / 1000))
        
        # Score de probabilidad (0-40 puntos)
        probability_score = probability * 40
        
        # Score de movimiento realista (0-30 puntos)
        # Penaliza movimientos muy grandes
        abs_change = abs(price_change)
        if abs_change < 5:
            movement_score = 30
        elif abs_change < 10:
            movement_score = 25
        elif abs_change < 20:
            movement_score = 15
        else:
            movement_score = 5
        
        total_score = liquidity_score + probability_score + movement_score
        return min(100, total_score)
    
    def plot_strategy(self, option_type, strike, premium, contracts=1):
        """
        Grafica el perfil de ganancia/pérdida de una estrategia
        
        Args:
            option_type (str): 'call' o 'put'
            strike (float): Precio de ejercicio
            premium (float): Prima pagada
            contracts (int): Número de contratos
        """
        if self.current_price is None:
            return
        
        # Rango de precios para graficar
        price_range = np.linspace(
            self.current_price * 0.7,
            self.current_price * 1.3,
            100
        )
        
        # Calcular P&L
        if option_type.lower() == 'call':
            payoff = np.maximum(price_range - strike, 0) - premium
        else:
            payoff = np.maximum(strike - price_range, 0) - premium
        
        payoff = payoff * 100 * contracts  # Convertir a dólares
        
        # Crear gráfico
        plt.figure(figsize=(12, 6))
        plt.plot(price_range, payoff, 'b-', linewidth=2, label=f'{option_type.upper()} ${strike}')
        plt.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Breakeven')
        plt.axvline(x=self.current_price, color='g', linestyle='--', alpha=0.5, label=f'Precio actual (${self.current_price:.2f})')
        
        # Marcar breakeven
        if option_type.lower() == 'call':
            breakeven_price = strike + premium
        else:
            breakeven_price = strike - premium
        plt.axvline(x=breakeven_price, color='orange', linestyle='--', alpha=0.5, label=f'Breakeven (${breakeven_price:.2f})')
        
        plt.xlabel('Precio de la Acción ($)', fontsize=12)
        plt.ylabel('Ganancia/Pérdida ($)', fontsize=12)
        plt.title(f'Perfil de P&L: {option_type.upper()} {self.ticker} ${strike} | {contracts} contrato(s)', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=10)
        
        # Añadir áreas de ganancia/pérdida
        plt.fill_between(price_range, 0, payoff, where=(payoff > 0), alpha=0.3, color='green', label='Zona de ganancia')
        plt.fill_between(price_range, 0, payoff, where=(payoff < 0), alpha=0.3, color='red', label='Zona de pérdida')
        
        plt.tight_layout()
        plt.show()
    
    def risk_calculator(self, investment_amount, max_loss_percent=10):
        """
        Calcula cuántos contratos comprar según tu tolerancia al riesgo
        
        Args:
            investment_amount (float): Capital total disponible
            max_loss_percent (float): Máximo % que estás dispuesto a perder
        """
        max_loss = investment_amount * (max_loss_percent / 100)
        
        print(f"\n{'='*60}")
        print(f"💰 CALCULADORA DE RIESGO")
        print(f"{'='*60}")
        print(f"Capital disponible: ${investment_amount:,.2f}")
        print(f"Máxima pérdida aceptable: {max_loss_percent}% = ${max_loss:,.2f}")
        print(f"\nRECOMENDACIONES:")
        print(f"  • Nunca arriesgues más del {max_loss_percent}% en una sola operación")
        print(f"  • Diversifica entre 3-5 operaciones diferentes")
        print(f"  • Por operación: máximo ${max_loss/3:,.2f}")
        print(f"  • Deja al menos 50% del capital como reserva")
        print(f"{'='*60}")

    def educational_summary(self):
        """Muestra un resumen educativo sobre opciones"""
        print(f"\n{'='*60}")
        print("📚 RESUMEN EDUCATIVO DE OPCIONES")
        print(f"{'='*60}")
        print("""
CONCEPTOS CLAVE:

1. CALL (Opción de Compra):
   - Comprás el derecho a COMPRAR a un precio fijo
   - Ganás si el precio SUBE por encima del strike + prima
   - Pérdida máxima: La prima que pagaste

2. PUT (Opción de Venta):
   - Comprás el derecho a VENDER a un precio fijo
   - Ganás si el precio BAJA por debajo del strike - prima
   - Pérdida máxima: La prima que pagaste

3. ELEMENTOS:
   - Strike: Precio de ejercicio
   - Premium: Costo de la opción (por acción)
   - Expiration: Fecha de vencimiento
   - 1 contrato = 100 acciones

4. BREAKEVEN:
   - CALL: Strike + Premium
   - PUT: Strike - Premium

5. RIESGOS:
   ⚠️  Puedes perder el 100% de lo invertido
   ⚠️  El tiempo trabaja en tu contra (decay)
   ⚠️  La volatilidad afecta los precios
   ⚠️  Requiere timing perfecto

6. CONSEJOS:
   ✓ Practica con simuladores primero
   ✓ Empieza con montos pequeños
   ✓ Estudia la empresa y el mercado
   ✓ No uses dinero que necesites
   ✓ Define tu estrategia de salida ANTES de entrar
        """)
        print(f"{'='*60}\n")


def main():
    """Función principal con menú interactivo"""
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║     SISTEMA DE ANÁLISIS DE OPCIONES FINANCIERAS       ║
    ║                  Versión Educativa 1.0                ║
    ╚═══════════════════════════════════════════════════════╝
    
    ⚠️  ADVERTENCIA IMPORTANTE:
    Este es un sistema educativo. El trading de opciones
    es extremadamente riesgoso. Puedes perder todo tu capital.
    
    Nunca inviertas dinero que no puedas perder.
    """)
    
    # Solicitar ticker
    ticker = input("\n📊 Ingresa el ticker a analizar (ej: AAPL, MSFT, TSLA): ").strip().upper()
    
    if not ticker:
        print("❌ Ticker inválido")
        return
    
    # Crear analizador
    analyzer = OptionsAnalyzer(ticker)
    
    if analyzer.current_price is None:
        print("❌ No se pudo obtener información del ticker")
        return
    
    while True:
        print(f"\n{'='*60}")
        print("MENÚ PRINCIPAL")
        print(f"{'='*60}")
        print("1. Analizar oportunidades de CALLs")
        print("2. Analizar oportunidades de PUTs")
        print("3. Ver cadena completa de opciones")
        print("4. Graficar estrategia específica")
        print("5. Calculadora de riesgo")
        print("6. Resumen educativo")
        print("7. Cambiar ticker")
        print("8. Salir")
        print(f"{'='*60}")
        
        choice = input("\nSelecciona una opción (1-8): ").strip()
        
        if choice == '1':
            target = float(input("Retorno objetivo deseado (ej: 1.0 = 100%, 0.5 = 50%): ") or "1.0")
            days = int(input("Días máximos hasta expiración (ej: 30): ") or "30")
            analyzer.analyze_option_opportunity('call', target, days)
            
        elif choice == '2':
            target = float(input("Retorno objetivo deseado (ej: 1.0 = 100%, 0.5 = 50%): ") or "1.0")
            days = int(input("Días máximos hasta expiración (ej: 30): ") or "30")
            analyzer.analyze_option_opportunity('put', target, days)
            
        elif choice == '3':
            calls, puts = analyzer.get_options_chain()
            if calls is not None:
                print("\n📞 CALLs (primeros 10):")
                print(calls[['strike', 'lastPrice', 'volume', 'openInterest']].head(10))
                print("\n📉 PUTs (primeros 10):")
                print(puts[['strike', 'lastPrice', 'volume', 'openInterest']].head(10))
            
        elif choice == '4':
            opt_type = input("Tipo (call/put): ").strip().lower()
            strike = float(input("Strike price: "))
            premium = float(input("Premium (precio por acción): "))
            contracts = int(input("Número de contratos: ") or "1")
            analyzer.plot_strategy(opt_type, strike, premium, contracts)
            
        elif choice == '5':
            capital = float(input("Capital disponible ($): "))
            risk = float(input("Máximo % a arriesgar (ej: 10): ") or "10")
            analyzer.risk_calculator(capital, risk)
            
        elif choice == '6':
            analyzer.educational_summary()
            
        elif choice == '7':
            ticker = input("Nuevo ticker: ").strip().upper()
            analyzer = OptionsAnalyzer(ticker)
            
        elif choice == '8':
            print("\n👋 ¡Gracias por usar el sistema! Recuerda: invierte responsablemente.")
            break
        
        else:
            print("❌ Opción inválida")


# Ejemplo de uso directo (sin menú interactivo)
if __name__ == "__main__":
    # Descomentar para usar el menú interactivo
    main()
    
    # O usar directamente:
    # analyzer = OptionsAnalyzer('AAPL')
    # analyzer.analyze_option_opportunity('call', target_return=1.0, days_to_expiry=30)
    # analyzer.plot_strategy('call', strike=240, premium=10, contracts=1)
```
