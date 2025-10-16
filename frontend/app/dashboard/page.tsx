'use client';

import { useQuery } from '@tanstack/react-query';
import { indexApi } from '@/lib/api';
import { IndexCard } from '@/components/index-card';
import { Loader2, AlertCircle, RefreshCw } from 'lucide-react';
import Link from 'next/link';

export default function DashboardPage() {
  const { data, isLoading, error, refetch, isRefetching } = useQuery({
    queryKey: ['index'],
    queryFn: indexApi.getIndex,
    refetchInterval: 30000, // Refetch every 30 seconds
  });

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-950">
      {/* Header */}
      <header className="border-b bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm sticky top-0 z-10">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div>
              <Link href="/" className="text-2xl font-bold hover:opacity-80 transition-opacity">
                📈 StockGenie
              </Link>
              <p className="text-sm text-muted-foreground mt-1">
                AI-Powered KSE100 Intelligence
              </p>
            </div>
            <button
              onClick={() => refetch()}
              disabled={isRefetching}
              className="flex items-center gap-2 px-4 py-2 rounded-lg bg-primary text-primary-foreground hover:opacity-90 transition-opacity disabled:opacity-50"
            >
              <RefreshCw className={`w-4 h-4 ${isRefetching ? 'animate-spin' : ''}`} />
              <span className="hidden sm:inline">Refresh</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold mb-2">
            KSE100 Index Dashboard
          </h1>
          <p className="text-muted-foreground">
            Real-time market data and insights
          </p>
        </div>

        {/* Loading State */}
        {isLoading && (
          <div className="flex flex-col items-center justify-center py-20">
            <Loader2 className="w-12 h-12 animate-spin text-primary mb-4" />
            <p className="text-lg text-muted-foreground">Loading market data...</p>
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="rounded-lg border border-red-200 bg-red-50 dark:bg-red-950/20 p-6">
            <div className="flex items-start gap-3">
              <AlertCircle className="w-6 h-6 text-red-600 dark:text-red-400 flex-shrink-0 mt-1" />
              <div className="flex-1">
                <h3 className="text-lg font-semibold text-red-900 dark:text-red-100 mb-1">
                  Failed to load market data
                </h3>
                <p className="text-red-700 dark:text-red-300 mb-4">
                  {error instanceof Error ? error.message : 'An unexpected error occurred'}
                </p>
                <button
                  onClick={() => refetch()}
                  className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
                >
                  Try Again
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Success State - Display Index Data */}
        {data && !isLoading && (
          <div className="space-y-6">
            <IndexCard data={data} />

            {/* Additional Info */}
            <div className="rounded-lg border bg-card p-6 shadow">
              <h2 className="text-xl font-semibold mb-4">About KSE100 Index</h2>
              <p className="text-muted-foreground mb-4">
                The KSE100 Index is a stock index comprising the top 100 companies listed on the Pakistan Stock Exchange 
                (PSX) based on market capitalization. It serves as a benchmark for the overall performance of the 
                Pakistani equity market.
              </p>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
                <div className="p-4 rounded-lg bg-muted/50">
                  <h3 className="font-semibold mb-2">📊 Constituent Companies</h3>
                  <p className="text-sm text-muted-foreground">
                    {data.constituent_count} leading companies across various sectors
                  </p>
                </div>
                <div className="p-4 rounded-lg bg-muted/50">
                  <h3 className="font-semibold mb-2">🎯 Market Coverage</h3>
                  <p className="text-sm text-muted-foreground">
                    Represents approximately 80% of total market capitalization
                  </p>
                </div>
              </div>
            </div>

            {/* Coming Soon */}
            <div className="rounded-lg border bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-950/20 dark:to-indigo-950/20 p-6">
              <h2 className="text-xl font-semibold mb-2">🚀 Coming Soon</h2>
              <ul className="space-y-2 text-muted-foreground">
                <li>✨ Sector performance breakdown</li>
                <li>📈 Top contributors and losers</li>
                <li>📊 Historical charts and trends</li>
                <li>🤖 AI-powered market insights</li>
              </ul>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t mt-20 py-6 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm">
        <div className="container mx-auto px-4 text-center text-sm text-muted-foreground">
          <p>© 2025 StockGenie. Professional stock analysis for Pakistani investors.</p>
        </div>
      </footer>
    </div>
  );
}

