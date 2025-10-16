/**
 * API Client for StockGenie Backend
 */
import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,
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

// Health check
export const healthApi = {
  check: async () => {
    const response = await api.get('/api/v1/health');
    return response.data;
  },
};

