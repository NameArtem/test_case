import pandas as pd

def calc_finrat(df_sorted):
    # доп.колонки для исследования
    df_sorted['gross_profit_margin'] = df_sorted['gross_profit'] / df_sorted['revenue']
    df_sorted['operating_profit_margin'] = df_sorted['operating_profit'] / df_sorted['revenue']
    df_sorted['net_profit_margin'] = df_sorted['net_profit'] / df_sorted['revenue']
    df_sorted['opex_to_revenue'] = df_sorted['opex'] / df_sorted['revenue']
    df_sorted['cost_of_goods_to_revenue'] = df_sorted['cost_of_goods'] / df_sorted['revenue']
    return df_sorted


def calc_yoy_growth(df_sorted):
    # расчет годового роста
    df_sorted['revenue_growth_yoy'] = df_sorted.groupby('company_id')['revenue'].pct_change() * 100
    df_sorted['net_profit_growth_yoy'] = df_sorted.groupby('company_id')['net_profit'].pct_change() * 100
    df_sorted['headcount_growth_yoy'] = df_sorted.groupby('company_id')['headcount'].pct_change() * 100
    return df_sorted


def calc_headcount(df_sorted):
    # Calculate revenue per headcount
    df_sorted['revenue_per_headcount'] = df_sorted['revenue'] / df_sorted['headcount']
    df_sorted['payroll_per_headcount'] = df_sorted['payroll_fund'] / df_sorted['headcount']
    return df_sorted


def format_rub(x, pos):
    if pd.isna(x):
        return ""
    if abs(x) >= 1_000_000_000:
        return f"{x/1_000_000_000:.1f}b"
    if abs(x) >= 1_000_000:
        return f"{x/1_000_000:.1f}m"
    if abs(x) >= 1_000:
        return f"{x/1_000:.1f}k"
    return f"{x:.0f}"