 # Parallel You Simulation Engine
def calculate_timeline(skill, hours_per_week):
    print("\n" + "="*50)
    print(f" SIMULATING TIMELINES FOR: {skill.upper()}")
    print(f" INVESTMENT: {hours_per_week} hours/week")
    print("="*50 + "\n")
    
    # Timeline A: Optimized / Consistent Route
    months_to_mastery_a = max(1, round(100 / (hours_per_week * 0.5), 1))
    print(f"📈 [Timeline A: The Optimized Path]")
    print(f"   - Outcome: Professional proficiency achieved.")
    print(f"   - Estimated Time: Approx. {months_to_mastery_a} months of strict consistency.")
    print(f"   - Risk: High mental burnout if rest isn't prioritized.\n")
    
    # Timeline B: Unpredictable / Chaotic Route
    months_to_mastery_b = max(1, round(months_to_mastery_a * 1.5, 1))
    print(f"⚡ [Timeline B: The Resilient Path]")
    print(f"   - Outcome: Real-world setbacks force practical adaptation.")
    print(f"   - Estimated Time: Approx. {months_to_mastery_b} months due to unexpected hurdles.")
    print(f"   - Perk: Exceptional real-world problem-solving skills built.\n")
    print("="*50)

if __name__ == "__main__":
    # Test simulation with default student parameters
    user_skill = input("Enter your core focus or skill (e.g., Computer Engineering): ")
    try:
        user_hours = float(input("Enter available hours per week: "))
    except ValueError:
        user_hours = 20 # Default fallback
        
    calculate_timeline(user_skill, user_hours)