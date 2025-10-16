/**
 * API Client for StockGenie Backend
 */
import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,  // Don't add /api/v1 here - it's in the endpoint paths
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Response types
export interface IndexData {
  symbol: string;
  name: string;
  value: number;
  change: number;
  change_percent: number;
  previous_close: number;
  open: number;
  high: number;
  low: number;
  volume: number;
  market_cap: number;
  year_high: number;
  year_low: number;
  ytd_change_percent: number;
  constituent_count: number;
  trading_status: string;
  timestamp: string;
  average_volume_30d?: number;
}

export interface SectorData {
  id: number;
  name: string;
  market_cap: number;
  weight_percent: number;
  companies_count: number;
  day_change_percent: number;
  avg_pe_ratio: number;
  color: string;
}

export interface CompanyData {
  rank: number;
  symbol: string;
  name: string;
  sector: string;
  price: number;
  change: number;
  change_percent: number;
  market_cap: number;
  pe_ratio: number;
  dividend_yield: number;
  eps: number;
  volume: number;
  year_high: number;
  year_low: number;
}

// API functions
export const indexApi = {
  /**
   * Get current KSE100 index data
   */
  getIndex: async (): Promise<IndexData> => {
    const response = await api.get<IndexData>('/api/v1/index/');
    return response.data;
  },
};

export const sectorsApi = {
  /**
   * Get all sectors
   */
  getSectors: async (): Promise<SectorData[]> => {
    const response = await api.get<SectorData[]>('/api/v1/sectors/');
    return response.data;
  },
};

export const companiesApi = {
  /**
   * Get top companies
   */
  getTopCompanies: async (limit: number = 30): Promise<CompanyData[]> => {
    const response = await api.get<CompanyData[]>(`/api/v1/companies/top?limit=${limit}`);
    return response.data;
  },
};

// Health check
export const healthApi = {
  check: async () => {
    const response = await api.get('/api/v1/health');
    return response.data;
  },
};

