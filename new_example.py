

df_xodimlar = pd.DataFrame({
    "Ism": ["Ali", "Vali"],
    "Bo'lim": ["IT", "Marketing"]
})

df_mahsulotlar = pd.DataFrame({
    "Mahsulot": ["Noutbuk", "Telefon"],
    "Narxi": [800, 500]
})

# ExcelWriter bilan bitta faylga yozish
with pd.ExcelWriter("kompaniya_hisoboti.xlsx") as writer:
    df_xodimlar.to_excel(writer, sheet_name="Xodimlar", index=False)
    df_mahsulotlar.to_excel(writer, sheet_name="Mahsulotlar", index=False)

print("Ko'p sahifali Excel fayli yaratildi!")