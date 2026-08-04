from pathlib import Path
import shutil

file = Path("src/pages/FuelSales.jsx")

# Backup
backup = Path("src/pages/FuelSales_before_python_fix.jsx")
shutil.copy(file, backup)

text = file.read_text()

# Cash
text = text.replace(
'''<input placeholder="Cash at Hand"
        value={cash}
        onChange={(e)=>setCash(e.target.value)}
      />''',
'''<input
        type="number"
        placeholder="Cash at Hand"
        value={cash}
        onChange={(e)=>setCash(e.target.value)}
      />'''
)

# POS
text = text.replace(
'''<input placeholder="POS Sales"
        value={pos}
        onChange={(e)=>setPos(e.target.value)}
      />''',
'''<input
        type="number"
        placeholder="POS Sales"
        value={pos}
        onChange={(e)=>setPos(e.target.value)}
      />'''
)

# Transfer
text = text.replace(
'''<input placeholder="Bank Transfer"
        value={transfer}
        onChange={(e)=>setTransfer(e.target.value)}
      />''',
'''<input
        type="number"
        placeholder="Bank Transfer"
        value={transfer}
        onChange={(e)=>setTransfer(e.target.value)}
      />'''
)

# Credit
text = text.replace(
'''<input placeholder="Credit Sales"
        value={credit}
        onChange={(e)=>setCredit(e.target.value)}
      />''',
'''<input
        type="number"
        placeholder="Credit Sales"
        value={credit}
        onChange={(e)=>setCredit(e.target.value)}
      />'''
)

# Expenses
text = text.replace(
'''<input placeholder="Expenses"
        value={expenses}
        onChange={(e)=>setExpenses(e.target.value)}
      />''',
'''<input
        type="number"
        placeholder="Expenses"
        value={expenses}
        onChange={(e)=>setExpenses(e.target.value)}
      />'''
)

# Add debug log before insert
old = '''const { error } = await supabase'''
new = '''console.log({
      stationId,
      cash,
      pos,
      transfer,
      credit,
      expenses
    });

    const { error } = await supabase'''

text = text.replace(old, new)

file.write_text(text)

print("✅ FuelSales.jsx updated successfully.")
print("✅ Backup created:", backup)
