import flet as ft


def main(page: ft.Page):
    page.tittle = "Calculadora"
    page.bgcolor="green"
    txtNum1=ft.TextField(label="Ingresa el primer número",color="yellow")
    txtNum2=ft.TextField(label="Ingresa el segundo número",color="yellow")
    lblResultado=ft.Text("Resultado: ",color="yellow")
    
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_calc_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click_division)
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
            ],alignment="center"),
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMultiplicacion,
            btnDivision
        ],alignment="center")
    )
ft.app(main)
