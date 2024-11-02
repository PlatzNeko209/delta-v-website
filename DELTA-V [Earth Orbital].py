import math

def calculate_delta_v(Isp, g0, m0, mf):
    """Calculate Delta-V using Tsiolkovsky Rocket Equation."""
    return Isp * g0 * math.log(m0 / mf)

def main():
    # Constants
    g0 = 9.81  # Standard gravity (m/s^2)

    # Orbital velocities
    LEO_velocity = 7800  # m/s
    MEO_velocity = 10200  # m/s
    HEO_velocity = 11000  # m/s

    while True:
        print("Welcome to the Delta-V Calculator!")

        try:
            # Input from the user
            Isp = float(input("Enter Isp (s): "))
            m0 = float(input("Enter m0 (tons): ")) * 1000  # Convert tons to kg
            mf = float(input("Enter mf (tons): ")) * 1000  # Convert tons to kg

            # Calculate Delta-V
            delta_v = calculate_delta_v(Isp, g0, m0, mf)

            # Display results
            print("\n--- Results ---")
            print(f"Delta V: {delta_v:.2f} m/s")

            # Check which orbit the rocket can reach
            if delta_v >= HEO_velocity:
                print("Your rocket can reach High Earth Orbit (HEO).")
            elif delta_v >= MEO_velocity:
                print("Your rocket can reach Medium Earth Orbit (MEO).")
            elif delta_v >= LEO_velocity:
                print("Your rocket can reach Low Earth Orbit (LEO).")
            else:
                print("Unfortunately, your rocket cannot reach any of the specified orbits.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask user if they want to reset
        reset = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if reset != 'yes':
            print("Thank you for using the Delta-V Calculator!")
            break

if __name__ == "__main__":
    main()