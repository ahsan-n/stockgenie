export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-center font-mono text-sm">
        <h1 className="text-4xl font-bold text-center mb-8">
          📈 StockGenie
        </h1>
        <p className="text-center text-xl mb-4">
          AI-Powered KSE100 Intelligence Platform
        </p>
        <p className="text-center text-muted-foreground">
          Coming Soon: Professional stock analysis for Pakistani investors
        </p>
        
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow">
            <h3 className="font-bold mb-2">📊 Real-time Data</h3>
            <p className="text-sm text-muted-foreground">
              KSE100 index tracking with live updates and sector analysis
            </p>
          </div>
          
          <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow">
            <h3 className="font-bold mb-2">📑 Financial Deep-Dive</h3>
            <p className="text-sm text-muted-foreground">
              10 years of financial statements and comprehensive ratios
            </p>
          </div>
          
          <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow">
            <h3 className="font-bold mb-2">🤖 AI Insights</h3>
            <p className="text-sm text-muted-foreground">
              Conversational analysis powered by advanced AI
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}

