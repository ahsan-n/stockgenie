"""
Mock financial statement data for development and testing
"""
from typing import List, Dict

# Mock Income Statements for FCCL (10 years)
MOCK_INCOME_STATEMENTS_FCCL = [
    {
        "period_end": "2023-12-31",
        "period_type": "annual",
        "revenue": 45_123_456_789,
        "cost_of_revenue": 30_500_000_000,
        "gross_profit": 14_623_456_789,
        "operating_expenses": 3_200_000_000,
        "operating_income": 11_423_456_789,
        "interest_expense": 500_000_000,
        "income_before_tax": 10_923_456_789,
        "income_tax": 923_456_789,
        "net_income": 10_000_000_000,
        "eps": 5.10,
    },
    {
        "period_end": "2022-12-31",
        "period_type": "annual",
        "revenue": 42_000_000_000,
        "cost_of_revenue": 28_500_000_000,
        "gross_profit": 13_500_000_000,
        "operating_expenses": 3_000_000_000,
        "operating_income": 10_500_000_000,
        "interest_expense": 480_000_000,
        "income_before_tax": 10_020_000_000,
        "income_tax": 870_000_000,
        "net_income": 9_150_000_000,
        "eps": 4.67,
    },
    {
        "period_end": "2021-12-31",
        "period_type": "annual",
        "revenue": 38_500_000_000,
        "cost_of_revenue": 26_000_000_000,
        "gross_profit": 12_500_000_000,
        "operating_expenses": 2_800_000_000,
        "operating_income": 9_700_000_000,
        "interest_expense": 450_000_000,
        "income_before_tax": 9_250_000_000,
        "income_tax": 800_000_000,
        "net_income": 8_450_000_000,
        "eps": 4.31,
    },
    # Additional years (simplified for brevity)
    {"period_end": "2020-12-31", "period_type": "annual", "revenue": 35_000_000_000, "net_income": 7_800_000_000, "eps": 3.98},
    {"period_end": "2019-12-31", "period_type": "annual", "revenue": 33_000_000_000, "net_income": 7_200_000_000, "eps": 3.67},
    {"period_end": "2018-12-31", "period_type": "annual", "revenue": 31_000_000_000, "net_income": 6_800_000_000, "eps": 3.47},
    {"period_end": "2017-12-31", "period_type": "annual", "revenue": 29_000_000_000, "net_income": 6_200_000_000, "eps": 3.16},
    {"period_end": "2016-12-31", "period_type": "annual", "revenue": 27_000_000_000, "net_income": 5_800_000_000, "eps": 2.96},
    {"period_end": "2015-12-31", "period_type": "annual", "revenue": 25_000_000_000, "net_income": 5_200_000_000, "eps": 2.65},
    {"period_end": "2014-12-31", "period_type": "annual", "revenue": 23_000_000_000, "net_income": 4_800_000_000, "eps": 2.45},
]

# Mock Balance Sheets for FCCL
MOCK_BALANCE_SHEETS_FCCL = [
    {
        "period_end": "2023-12-31",
        "period_type": "annual",
        "total_assets": 75_000_000_000,
        "current_assets": 25_000_000_000,
        "non_current_assets": 50_000_000_000,
        "total_liabilities": 45_000_000_000,
        "current_liabilities": 15_000_000_000,
        "non_current_liabilities": 30_000_000_000,
        "shareholders_equity": 30_000_000_000,
    },
    {
        "period_end": "2022-12-31",
        "period_type": "annual",
        "total_assets": 70_000_000_000,
        "current_assets": 23_000_000_000,
        "non_current_assets": 47_000_000_000,
        "total_liabilities": 42_000_000_000,
        "current_liabilities": 14_000_000_000,
        "non_current_liabilities": 28_000_000_000,
        "shareholders_equity": 28_000_000_000,
    },
    # Simplified for other years
    {"period_end": "2021-12-31", "period_type": "annual", "total_assets": 65_000_000_000, "shareholders_equity": 26_000_000_000},
    {"period_end": "2020-12-31", "period_type": "annual", "total_assets": 60_000_000_000, "shareholders_equity": 24_000_000_000},
]

# Mock Cash Flow Statements for FCCL
MOCK_CASHFLOW_STATEMENTS_FCCL = [
    {
        "period_end": "2023-12-31",
        "period_type": "annual",
        "operating_cashflow": 12_000_000_000,
        "investing_cashflow": -3_500_000_000,
        "financing_cashflow": -2_000_000_000,
        "free_cashflow": 8_500_000_000,
        "capex": 3_500_000_000,
    },
    {
        "period_end": "2022-12-31",
        "period_type": "annual",
        "operating_cashflow": 11_000_000_000,
        "investing_cashflow": -3_000_000_000,
        "financing_cashflow": -1_800_000_000,
        "free_cashflow": 8_000_000_000,
        "capex": 3_000_000_000,
    },
]

# Mock Financial Ratios for FCCL
MOCK_FINANCIAL_RATIOS_FCCL = [
    {
        "period_end": "2023-12-31",
        "pe_ratio": 4.50,
        "pb_ratio": 1.67,
        "roe": 33.33,
        "roa": 13.33,
        "debt_to_equity": 1.50,
        "current_ratio": 1.67,
        "dividend_yield": 8.24,
        "profit_margin": 22.16,
    },
    {
        "period_end": "2022-12-31",
        "pe_ratio": 4.80,
        "pb_ratio": 1.75,
        "roe": 32.68,
        "roa": 13.07,
        "debt_to_equity": 1.50,
        "current_ratio": 1.64,
        "dividend_yield": 7.80,
        "profit_margin": 21.79,
    },
]


def get_mock_income_statements(symbol: str, period_type: str = "annual") -> List[Dict]:
    """Get mock income statements"""
    if symbol == "FCCL":
        return MOCK_INCOME_STATEMENTS_FCCL
    return []


def get_mock_balance_sheets(symbol: str, period_type: str = "annual") -> List[Dict]:
    """Get mock balance sheets"""
    if symbol == "FCCL":
        return MOCK_BALANCE_SHEETS_FCCL
    return []


def get_mock_cashflow_statements(symbol: str, period_type: str = "annual") -> List[Dict]:
    """Get mock cash flow statements"""
    if symbol == "FCCL":
        return MOCK_CASHFLOW_STATEMENTS_FCCL
    return []


def get_mock_financial_ratios(symbol: str) -> List[Dict]:
    """Get mock financial ratios"""
    if symbol == "FCCL":
        return MOCK_FINANCIAL_RATIOS_FCCL
    return []

