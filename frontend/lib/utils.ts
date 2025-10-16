import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

/**
 * Format number with commas for thousands
 */
export function formatNumber(num: number, decimals: number = 2): string {
  return num.toLocaleString('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

/**
 * Format currency in PKR
 */
export function formatCurrency(amount: number, compact: boolean = false): string {
  if (compact && amount >= 1_000_000_000_000) {
    return `PKR ${(amount / 1_000_000_000_000).toFixed(2)}T`;
  }
  if (compact && amount >= 1_000_000_000) {
    return `PKR ${(amount / 1_000_000_000).toFixed(2)}B`;
  }
  if (compact && amount >= 1_000_000) {
    return `PKR ${(amount / 1_000_000).toFixed(2)}M`;
  }
  return `PKR ${formatNumber(amount, 0)}`;
}

/**
 * Format volume with abbreviations
 */
export function formatVolume(volume: number): string {
  if (volume >= 1_000_000_000) {
    return `${(volume / 1_000_000_000).toFixed(2)}B`;
  }
  if (volume >= 1_000_000) {
    return `${(volume / 1_000_000).toFixed(2)}M`;
  }
  if (volume >= 1_000) {
    return `${(volume / 1_000).toFixed(2)}K`;
  }
  return volume.toString();
}

/**
 * Get color class for positive/negative change
 */
export function getChangeColor(change: number): string {
  if (change > 0) return 'text-green-600 dark:text-green-400';
  if (change < 0) return 'text-red-600 dark:text-red-400';
  return 'text-gray-600 dark:text-gray-400';
}

/**
 * Get background color for positive/negative change
 */
export function getChangeBgColor(change: number): string {
  if (change > 0) return 'bg-green-50 dark:bg-green-950/20';
  if (change < 0) return 'bg-red-50 dark:bg-red-950/20';
  return 'bg-gray-50 dark:bg-gray-950/20';
}

