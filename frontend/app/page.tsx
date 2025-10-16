import Link from 'next/link';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 md:p-24 bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-950">
      <div className="z-10 max-w-5xl w-full items-center justify-center">
        <h1 className="text-4xl md:text-6xl font-bold text-center mb-4">
          📈 StockGenie
        </h1>
        <p className="text-center text-xl md:text-2xl mb-2">
          AI-Powered KSE100 Intelligence Platform
        </p>
        <p className="text-center text-muted-foreground mb-8">
          Professional stock analysis for Pakistani investors
        </p>
        
        <div className="flex justify-center mb-12">
          <Link 
            href="/dashboard"
            className="px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white text-lg font-semibold rounded-lg shadow-lg transition-all hover:scale-105"
          >
            View Dashboard →
          </Link>
        </div>
        
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow bg-white dark:bg-gray-800">
            <h3 className="font-bold mb-2 text-lg">📊 Real-time Data</h3>
            <p className="text-sm text-muted-foreground">
              KSE100 index tracking with live updates and sector analysis
            </p>
          </div>
          
          <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow bg-white dark:bg-gray-800">
            <h3 className="font-bold mb-2 text-lg">📑 Financial Deep-Dive</h3>
            <p className="text-sm text-muted-foreground">
              10 years of financial statements and comprehensive ratios
            </p>
          </div>
          
          <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow bg-white dark:bg-gray-800">
            <h3 className="font-bold mb-2 text-lg">🤖 AI Insights</h3>
            <p className="text-sm text-muted-foreground">
              Conversational analysis powered by advanced AI
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}

