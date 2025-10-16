'use client';

import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';
import { SectorData } from '@/lib/api';

interface SectorPieChartProps {
  sectors: SectorData[];
  onSectorClick?: (sector: SectorData) => void;
}

export function SectorPieChart({ sectors, onSectorClick }: SectorPieChartProps) {
  // Prepare data for pie chart
  const chartData = sectors.map(sector => ({
    name: sector.name,
    value: sector.weight_percent,
    market_cap: sector.market_cap,
    color: sector.color,
    full: sector,
  }));

  const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      const data = payload[0].payload;
      return (
        <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700">
          <p className="font-bold text-gray-900 dark:text-white mb-2">{data.name}</p>
          <p className="text-sm text-gray-600 dark:text-gray-300">
            Weight: <span className="font-semibold">{data.value.toFixed(1)}%</span>
          </p>
          <p className="text-sm text-gray-600 dark:text-gray-300">
            Market Cap: <span className="font-semibold">PKR {(data.market_cap / 1e9).toFixed(0)}B</span>
          </p>
        </div>
      );
    }
    return null;
  };

  const handleClick = (data: any) => {
    if (onSectorClick && data.full) {
      onSectorClick(data.full);
    }
  };

  return (
    <div className="w-full h-[400px]">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={chartData}
            cx="50%"
            cy="50%"
            labelLine={false}
            label={({ name, value }) => `${name.split(' ')[0]} ${value.toFixed(1)}%`}
            outerRadius={120}
            fill="#8884d8"
            dataKey="value"
            onClick={handleClick}
            style={{ cursor: onSectorClick ? 'pointer' : 'default' }}
          >
            {chartData.map((entry, index) => (
              <Cell 
                key={`cell-${index}`} 
                fill={entry.color}
                className="hover:opacity-80 transition-opacity"
              />
            ))}
          </Pie>
          <Tooltip content={<CustomTooltip />} />
          <Legend 
            verticalAlign="bottom" 
            height={36}
            formatter={(value) => <span className="text-sm">{value}</span>}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

