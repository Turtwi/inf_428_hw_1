import pandas as pd
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportions_ztest  # Corrected import

def load_data(file_path):
    # Load the CSV file into a DataFrame and return it
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def calculate_conversion_rates(data, group_col='user_type', conversion_col='is_converted'):
    # Group the data by control and treatment, then calculate conversion rates
    conversion_summary = data.groupby(group_col)[conversion_col].agg(['sum', 'count'])
    conversion_summary['conversion_rate'] = conversion_summary['sum'] / conversion_summary['count']
    return conversion_summary

def perform_ab_test(data, group_col='user_type', conversion_col='is_converted'):
    # Perform a chi-square test to check for significant differences
    contingency_table = pd.crosstab(data[group_col], data[conversion_col])
    _, p_value, _, _ = chi2_contingency(contingency_table)
    return p_value

def perform_z_test(data, group_col='user_type', conversion_col='is_converted'):
    # Perform a Z-test for proportions
    conversion_summary = data.groupby(group_col)[conversion_col].agg(['sum', 'count'])
    counts = conversion_summary['sum'].values
    nobs = conversion_summary['count'].values
    _, p_value = proportions_ztest(counts, nobs)
    return p_value

def analyze_and_compare(experimental_data, historical_data, group_col='user_type', conversion_col='is_converted'):
    print("\nComparing Experimental and Historical Data")

    # Calculate conversion rates for both datasets
    experimental_rates = calculate_conversion_rates(experimental_data, group_col, conversion_col)
    historical_rates = calculate_conversion_rates(historical_data, group_col, conversion_col)

    print("\nExperimental Conversion Rates:")
    print(experimental_rates)

    print("\nHistorical Conversion Rates:")
    print(historical_rates)

    # Perform chi-square tests
    exp_p_value = perform_ab_test(experimental_data, group_col, conversion_col)
    hist_p_value = perform_ab_test(historical_data, group_col, conversion_col)

    print(f"\nExperimental Chi-Square Test p-value: {exp_p_value}")
    print(f"Historical Chi-Square Test p-value: {hist_p_value}")

    # Compare overall conversion rates
    exp_overall_rate = experimental_data[conversion_col].mean()
    hist_overall_rate = historical_data[conversion_col].mean()

    print(f"\nOverall Experimental Conversion Rate: {exp_overall_rate:.4f}")
    print(f"Overall Historical Conversion Rate: {hist_overall_rate:.4f}")

    # Decision criteria: check if experimental improves by at least 2% and is statistically significant
    improvement_threshold = 0.02
    improvement = exp_overall_rate - hist_overall_rate

    if exp_p_value < 0.05 and improvement > improvement_threshold:
        print(f"\nDecision: Adopt Experimental. Improvement of {improvement:.2%} is significant.")
        return "Adopt Experimental"
    else:
        print(f"\nDecision: Keep Historical. Improvement of {improvement:.2%} is not significant or too small.")
        return "Keep Historical"

def main():
    # Paths for experimental and historical files
    experimental_files = {
        'New Checkout Design': '[experimental]-A-B-test-new-checkout-design.csv',
        'New Color Palette': '[experimental]-A-B-test-new-color-palette.csv',
        'New ML Algorithm': '[experimental]-A-B-test-new-ml-recommendation-system.csv'
    }

    historical_files = {
        'New Checkout Design': '[historical]-A-B-test-new-checkout-design.csv',
        'New Color Palette': '[historical]-A-B-test-new-cnew-color-palette.csv',
        'New ML Algorithm': '[historical]-A-B-test-new-ml-recommendation-system.csv'
    }

    for experiment in experimental_files.keys():
        print(f"\n=== Experiment: {experiment} ===")
        exp_file = experimental_files[experiment]
        hist_file = historical_files[experiment]

        exp_data = load_data(exp_file)
        hist_data = load_data(hist_file)

        if exp_data is not None and hist_data is not None:
            decision = analyze_and_compare(exp_data, hist_data)
            print(f"Final Decision for {experiment}: {decision}")
        else:
            print(f"Skipping {experiment} due to data loading issues.")

if __name__ == "__main__":
    main()

