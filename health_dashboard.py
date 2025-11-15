# ============================================
# HEALTH & LIFESTYLE DASHBOARD
# Personal wellness tracking calculator
# Created by: Misbah
# Date: 15 November 2024
# Language: Python
# GitHub: Misbah-riaz5
# ============================================

print("=" * 50)
print("      HEALTH & LIFESTYLE DASHBOARD v1.0")
print("=" * 50)
print("\nTrack your daily habits and see long-term projections!")

# === USER INPUT ===
print("\n" + "-" * 55)
print("STEP 1: Enter Your Information")
print("-" * 55)

name = input("\n👤 Your name: ")
age = int(input("🎂 Your age: "))
siblings = int(input("👨‍👩‍👧‍👦 Number of siblings: "))

print("\n" + "-" * 55)
print("STEP 2: Daily Habits")
print("-" * 55)

cups_of_coffee = int(input("\n☕ Cups of coffee per day: "))
calories_daily = float(input("🍎 Daily calories consumed: "))
exercise_daily = int(input("💪 Daily exercise (minutes): "))

# === CALCULATIONS ===
# Coffee tracking
cups_monthly = cups_of_coffee * 30
cups_yearly = cups_of_coffee * 365

# Calorie tracking
calories_weekly = calories_daily * 7
calories_monthly = calories_daily * 30
calories_yearly = calories_daily * 365

# Exercise tracking
exercise_weekly = exercise_daily * 7
exercise_monthly_mins = exercise_daily * 30
exercise_monthly_hours = exercise_monthly_mins / 60
exercise_yearly_mins = exercise_daily * 365
exercise_yearly_hours = exercise_yearly_mins / 60

# Health recommendations
recommended_exercise_monthly = 150 * 4  # 150 mins/week recommended

# === DISPLAY DASHBOARD ===
print("\n" + "=" * 55)
print(f"     {name.upper()}'S WELLNESS REPORT")
print("=" * 55)

# Personal Info Section
print("\n📋 PERSONAL INFORMATION:")
print(f"   Name: {name}")
print(f"   Age: {age} years")
print(f"   Siblings: {siblings}")

# Coffee Section
print("\n☕ COFFEE CONSUMPTION ANALYSIS:")
print(f"   Daily:   {cups_of_coffee} cups")
print(f"   Monthly: {cups_monthly} cups")
print(f"   Yearly:  {cups_yearly} cups")
print(f"   💡 Note: Recommended max is 3-4 cups/day")

# Nutrition Section
print("\n🍎 NUTRITION TRACKING:")
print(f"   Daily:   {calories_daily:.0f} calories")
print(f"   Weekly:  {calories_weekly:.0f} calories")
print(f"   Monthly: {calories_monthly:.0f} calories")
print(f"   Yearly:  {calories_yearly:.0f} calories")

# Exercise Section
print("\n💪 EXERCISE STATISTICS:")
print(f"   Daily:   {exercise_daily} minutes")
print(f"   Weekly:  {exercise_weekly} minutes")
print(f"   Monthly: {exercise_monthly_mins} mins ({exercise_monthly_hours:.1f} hours)")
print(f"   Yearly:  {exercise_yearly_mins} mins ({exercise_yearly_hours:.1f} hours)")
print(f"   💡 WHO Recommended: {recommended_exercise_monthly} mins/month")

# Summary Section
print("\n" + "=" * 55)
print("                  SUMMARY")
print("=" * 55)
print(f"In one year, you will:")
print(f"  • Drink {cups_yearly} cups of coffee ☕")
print(f"  • Consume {calories_yearly:.0f} calories 🍎")
print(f"  • Exercise for {exercise_yearly_hours:.0f} hours 💪")
print("\n" + "=" * 55)
print("    Stay consistent! Small habits = Big results 🚀")
print("=" * 55)