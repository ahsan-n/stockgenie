'use client';

import { IndexData } from '@/lib/api';
import { formatNumber, formatCurrency, formatVolume, getChangeColor, getChangeBgColor } from '@/lib/utils';
import { TrendingUp, TrendingDown, Activity, BarChart3, Clock } from 'lucide-react';
import { format } from 'date-fns';

interface IndexCardProps {
  data: IndexData;
}

export function IndexCard({ data }: IndexCardProps) {
  const isPositive = data.change >= 0;
  const Icon = isPositive ? TrendingUp : TrendingDown;

  return (
    <div className="w-full">
      {/* Main Index Card */}
      <div className={`rounded-lg border bg-card text-card-foreground shadow-lg ${getChangeBgColor(data.change)} transition-all duration-300`}>
        <div className="p-6 md:p-8">
          {/* Header */}
          <div className="flex items-start justify-between mb-6">
            <div>
              <h2 className="text-sm font-medium text-muted-foreground mb-1">
                {data.symbol}
              </h2>
              <h1 className="text-2xl md:text-3xl font-bold">
                {data.name}
              </h1>
            </div>
            <div className={`p-3 rounded-full ${isPositive ? 'bg-green-100 dark:bg-green-900/30' : 'bg-red-100 dark:bg-red-900/30'}`}>
              <Icon className={`w-6 h-6 ${isPositive ? 'text-green-600 dark:text-green-400' : 'text-red-600 dark:text-red-400'}`} />
            </div>
          </div>

          {/* Current Value */}
          <div className="mb-6">
            <div className="text-5xl md:text-6xl font-bold mb-2">
              {formatNumber(data.value, 2)}
            </div>
            <div className={`flex items-center gap-2 text-xl md:text-2xl font-semibold ${getChangeColor(data.change)}`}>
              <span>{isPositive ? '+' : ''}{formatNumber(data.change, 2)}</span>
              <span>({isPositive ? '+' : ''}{formatNumber(data.change_percent, 2)}%)</span>
            </div>
          </div>

          {/* Key Metrics Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-6 border-t">
            <div>
              <p className="text-xs text-muted-foreground mb-1">Open</p>
              <p className="text-lg font-semibold">{formatNumber(data.open, 2)}</p>
            </div>
            <div>
              <p className="text-xs text-muted-foreground mb-1">High</p>
              <p className="text-lg font-semibold text-green-600 dark:text-green-400">{formatNumber(data.high, 2)}</p>
            </div>
            <div>
              <p className="text-xs text-muted-foreground mb-1">Low</p>
              <p className="text-lg font-semibold text-red-600 dark:text-red-400">{formatNumber(data.low, 2)}</p>
            </div>
            <div>
              <p className="text-xs text-muted-foreground mb-1">Prev Close</p>
              <p className="text-lg font-semibold">{formatNumber(data.previous_close, 2)}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Secondary Info Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
        {/* Market Cap */}
        <div className="rounded-lg border bg-card p-4 shadow">
          <div className="flex items-center gap-2 mb-2">
            <BarChart3 className="w-4 h-4 text-muted-foreground" />
            <p className="text-sm text-muted-foreground">Market Cap</p>
          </div>
          <p className="text-2xl font-bold">{formatCurrency(data.market_cap, true)}</p>
        </div>

        {/* Volume */}
        <div className="rounded-lg border bg-card p-4 shadow">
          <div className="flex items-center gap-2 mb-2">
            <Activity className="w-4 h-4 text-muted-foreground" />
            <p className="text-sm text-muted-foreground">Volume</p>
          </div>
          <p className="text-2xl font-bold">{formatVolume(data.volume)}</p>
          {data.average_volume_30d && (
            <p className="text-xs text-muted-foreground mt-1">
              Avg: {formatVolume(data.average_volume_30d)}
            </p>
          )}
        </div>

        {/* 52-Week Range */}
        <div className="rounded-lg border bg-card p-4 shadow">
          <div className="flex items-center gap-2 mb-2">
            <TrendingUp className="w-4 h-4 text-muted-foreground" />
            <p className="text-sm text-muted-foreground">52-Week Range</p>
          </div>
          <p className="text-lg font-semibold">
            {formatNumber(data.year_low, 0)} - {formatNumber(data.year_high, 0)}
          </p>
          <p className={`text-xs mt-1 ${getChangeColor(data.ytd_change_percent)}`}>
            YTD: {data.ytd_change_percent > 0 ? '+' : ''}{formatNumber(data.ytd_change_percent, 2)}%
          </p>
        </div>
      </div>

      {/* Status Bar */}
      <div className="mt-4 rounded-lg border bg-card p-3 shadow flex items-center justify-between text-sm">
        <div className="flex items-center gap-2">
          <Clock className="w-4 h-4 text-muted-foreground" />
          <span className="text-muted-foreground">Last Updated:</span>
          <span className="font-medium">{format(new Date(data.timestamp), 'PPpp')}</span>
        </div>
        <div className="flex items-center gap-2">
          <div className={`w-2 h-2 rounded-full ${data.trading_status === 'open' ? 'bg-green-500' : 'bg-red-500'} animate-pulse`} />
          <span className="font-medium capitalize">{data.trading_status}</span>
        </div>
      </div>
    </div>
  );
}

