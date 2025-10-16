'use client';

import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import { sectorsApi, companiesApi, SectorData, CompanyData } from '@/lib/api';
import { SectorPieChart } from '@/components/sector-pie-chart';
import { CompaniesTable } from '@/components/companies-table';

export default function SectorsPage() {
  const [selectedSector, setSelectedSector] = useState<SectorData | null>(null);

  // Fetch sectors
  const { data: sectors, isLoading: sectorsLoading, error: sectorsError } = useQuery({
    queryKey: ['sectors'],
    queryFn: sectorsApi.getSectors,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  // Fetch all companies
  const { data: companies, isLoading: companiesLoading } = useQuery({
    queryKey: ['companies'],
    queryFn: () => companiesApi.getTopCompanies(30),
    staleTime: 5 * 60 * 1000,
  });

  const handleSectorClick = (sector: SectorData) => {
    setSelectedSector(selectedSector?.id === sector.id ? null : sector);
  };

  const handleClearSelection = () => {
    setSelectedSector(null);
  };

  // Filter companies by selected sector
  const filteredCompanies = selectedSector && companies
    ? companies.filter(c => c.sector === selectedSector.name)
    : companies || [];

  const tableTitle = selectedSector 
    ? `${selectedSector.name} Companies`
    : 'Top 30 Companies by Market Cap';

  return (
    <main className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-950">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
            📊 KSE100 Sector Analysis
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Interactive sector composition and top companies
          </p>
        </div>

        {/* Sector Pie Chart */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-8">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
              Sector Composition
            </h2>
            {selectedSector && (
              <button
                onClick={handleClearSelection}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
              >
                Clear Selection
              </button>
            )}
          </div>

          {sectorsLoading && (
            <div className="flex items-center justify-center h-[400px]">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
            </div>
          )}

          {sectorsError && (
            <div className="flex items-center justify-center h-[400px]">
              <div className="text-red-600 dark:text-red-400">
                Failed to load sector data
              </div>
            </div>
          )}

          {sectors && (
            <>
              <SectorPieChart 
                sectors={sectors} 
                onSectorClick={handleSectorClick}
              />
              
              {selectedSector && (
                <div className="mt-4 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
                  <h3 className="font-bold text-lg text-blue-900 dark:text-blue-100 mb-2">
                    {selectedSector.name}
                  </h3>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                    <div>
                      <span className="text-gray-600 dark:text-gray-400">Weight:</span>
                      <span className="ml-2 font-semibold text-gray-900 dark:text-white">
                        {selectedSector.weight_percent}%
                      </span>
                    </div>
                    <div>
                      <span className="text-gray-600 dark:text-gray-400">Market Cap:</span>
                      <span className="ml-2 font-semibold text-gray-900 dark:text-white">
                        PKR {(selectedSector.market_cap / 1e9).toFixed(0)}B
                      </span>
                    </div>
                    <div>
                      <span className="text-gray-600 dark:text-gray-400">Companies:</span>
                      <span className="ml-2 font-semibold text-gray-900 dark:text-white">
                        {selectedSector.companies_count}
                      </span>
                    </div>
                    <div>
                      <span className="text-gray-600 dark:text-gray-400">Avg P/E:</span>
                      <span className="ml-2 font-semibold text-gray-900 dark:text-white">
                        {selectedSector.avg_pe_ratio.toFixed(1)}
                      </span>
                    </div>
                  </div>
                </div>
              )}
            </>
          )}
        </div>

        {/* Companies Table */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
          {companiesLoading && (
            <div className="flex items-center justify-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
            </div>
          )}

          {companies && (
            <CompaniesTable 
              companies={filteredCompanies}
              title={tableTitle}
            />
          )}
        </div>

        {/* Back to Dashboard */}
        <div className="mt-8 text-center">
          <a
            href="/dashboard"
            className="inline-block px-6 py-3 bg-gray-600 hover:bg-gray-700 text-white rounded-lg transition-colors"
          >
            ← Back to Dashboard
          </a>
        </div>
      </div>
    </main>
  );
}

