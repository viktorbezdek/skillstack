#!/usr/bin/env python3
"""
LLM Cost Calculator

Calculate and compare costs across different LLM providers.
"""

import argparse
from dataclasses import dataclass
from typing import Dict, List
import sys


# Pricing per 1M tokens (as of January 2025)
PRICING = {
    "gpt-4-turbo": {"input": 10.00, "output": 30.00, "provider": "OpenAI"},
    "gpt-4o": {"input": 5.00, "output": 15.00, "provider": "OpenAI"},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50, "provider": "OpenAI"},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00, "provider": "Anthropic", "cache": 0.30},
    "claude-3-opus": {"input": 15.00, "output": 75.00, "provider": "Anthropic", "cache": 1.50},
    "claude-3-haiku": {"input": 0.25, "output": 1.25, "provider": "Anthropic", "cache": 0.03},
    "gemini-1.5-pro": {"input": 1.25, "output": 5.00, "provider": "Google", "input_large": 2.50, "output_large": 10.00},
    "gemini-1.5-flash": {"input": 0.075, "output": 0.30, "provider": "Google", "input_large": 0.15, "output_large": 0.60},
}


@dataclass
class CostEstimate:
    """Cost estimate for a specific model."""
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    requests: int
    input_cost: float
    output_cost: float
    total_cost: float
    cache_savings: float = 0.0


def calculate_cost(
    model: str,
    input_tokens: int,
    output_tokens: int,
    requests: int = 1,
    cache_hit_rate: float = 0.0
) -> CostEstimate:
    """
    Calculate cost for a specific model.

    Args:
        model: Model name
        input_tokens: Input tokens per request
        output_tokens: Output tokens per request
        requests: Number of requests
        cache_hit_rate: Fraction of input tokens cached (0.0-1.0, Anthropic only)

    Returns:
        CostEstimate with detailed cost breakdown
    """
    if model not in PRICING:
        raise ValueError(f"Unknown model: {model}. Available: {list(PRICING.keys())}")

    pricing = PRICING[model]
    provider = pricing["provider"]

    # Calculate base costs
    total_input_tokens = input_tokens * requests
    total_output_tokens = output_tokens * requests

    # Gemini tiered pricing
    if provider == "Google" and "input_large" in pricing:
        if input_tokens > 128000:
            input_price = pricing["input_large"]
            output_price = pricing["output_large"]
        else:
            input_price = pricing["input"]
            output_price = pricing["output"]
    else:
        input_price = pricing["input"]
        output_price = pricing["output"]

    # Calculate input cost
    input_cost = (total_input_tokens / 1_000_000) * input_price

    # Calculate cache savings (Anthropic only)
    cache_savings = 0.0
    if provider == "Anthropic" and cache_hit_rate > 0:
        cached_tokens = total_input_tokens * cache_hit_rate
        cache_price = pricing.get("cache", 0)
        regular_cost = (cached_tokens / 1_000_000) * input_price
        cache_cost = (cached_tokens / 1_000_000) * cache_price
        cache_savings = regular_cost - cache_cost
        input_cost = input_cost - cache_savings

    # Calculate output cost
    output_cost = (total_output_tokens / 1_000_000) * output_price

    total_cost = input_cost + output_cost

    return CostEstimate(
        model=model,
        provider=provider,
        input_tokens=total_input_tokens,
        output_tokens=total_output_tokens,
        requests=requests,
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=total_cost,
        cache_savings=cache_savings
    )


def compare_models(
    models: List[str],
    input_tokens: int,
    output_tokens: int,
    requests: int = 1,
    cache_hit_rate: float = 0.0
) -> List[CostEstimate]:
    """
    Compare costs across multiple models.

    Args:
        models: List of model names
        input_tokens: Input tokens per request
        output_tokens: Output tokens per request
        requests: Number of requests
        cache_hit_rate: Cache hit rate for Anthropic models

    Returns:
        List of CostEstimate, sorted by total cost
    """
    estimates = []

    for model in models:
        try:
            estimate = calculate_cost(
                model=model,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                requests=requests,
                cache_hit_rate=cache_hit_rate if PRICING[model]["provider"] == "Anthropic" else 0.0
            )
            estimates.append(estimate)
        except ValueError as e:
            print(f"Warning: {e}", file=sys.stderr)

    # Sort by cost (ascending)
    estimates.sort(key=lambda e: e.total_cost)

    return estimates


def print_estimate(estimate: CostEstimate, detailed: bool = False):
    """Print a single cost estimate."""
    print(f"\n{'='*60}")
    print(f"Model: {estimate.model} ({estimate.provider})")
    print(f"{'='*60}")

    if detailed:
        print(f"Input tokens:  {estimate.input_tokens:,}")
        print(f"Output tokens: {estimate.output_tokens:,}")
        print(f"Requests:      {estimate.requests:,}")
        print(f"-" * 60)

    print(f"Input cost:    ${estimate.input_cost:,.4f}")
    print(f"Output cost:   ${estimate.output_cost:,.4f}")

    if estimate.cache_savings > 0:
        print(f"Cache savings: ${estimate.cache_savings:,.4f}")

    print(f"{'='*60}")
    print(f"Total cost:    ${estimate.total_cost:,.2f}")
    print(f"{'='*60}")


def print_comparison(estimates: List[CostEstimate]):
    """Print comparison table of estimates."""
    print(f"\n{'='*80}")
    print(f"{'Model':<25} {'Provider':<12} {'Total Cost':<15} {'Savings vs Cheapest':<20}")
    print(f"{'='*80}")

    if not estimates:
        print("No estimates to compare")
        return

    cheapest = estimates[0].total_cost

    for estimate in estimates:
        savings = estimate.total_cost - cheapest
        savings_pct = (savings / estimate.total_cost * 100) if estimate.total_cost > 0 else 0

        print(
            f"{estimate.model:<25} "
            f"{estimate.provider:<12} "
            f"${estimate.total_cost:>13,.2f} "
            f"+${savings:>8,.2f} ({savings_pct:>5.1f}%)"
        )

    print(f"{'='*80}")
    print(f"Cheapest: {estimates[0].model} at ${estimates[0].total_cost:,.2f}")
    print(f"Most expensive: {estimates[-1].model} at ${estimates[-1].total_cost:,.2f}")
    print(f"{'='*80}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Calculate and compare LLM API costs across providers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Calculate cost for single model
  python cost-calculator.py --model gpt-4-turbo --input 1000 --output 500

  # Calculate cost for 1000 requests
  python cost-calculator.py --model claude-3-5-sonnet --input 2000 --output 800 --requests 1000

  # Compare multiple models
  python cost-calculator.py --compare --input 1500 --output 600 --requests 500

  # Compare with cache hit rate (Anthropic only)
  python cost-calculator.py --compare --input 5000 --output 1000 --cache 0.8

  # Compare specific models
  python cost-calculator.py --compare --models gpt-4-turbo claude-3-5-sonnet --input 1000 --output 500
        """
    )

    parser.add_argument(
        "--model",
        type=str,
        help=f"Model to calculate cost for. Available: {', '.join(PRICING.keys())}"
    )

    parser.add_argument(
        "--compare",
        action="store_true",
        help="Compare costs across multiple models"
    )

    parser.add_argument(
        "--models",
        type=str,
        nargs="+",
        help="Specific models to compare (use with --compare)"
    )

    parser.add_argument(
        "--input",
        type=int,
        required=True,
        help="Input tokens per request"
    )

    parser.add_argument(
        "--output",
        type=int,
        required=True,
        help="Output tokens per request"
    )

    parser.add_argument(
        "--requests",
        type=int,
        default=1,
        help="Number of requests (default: 1)"
    )

    parser.add_argument(
        "--cache",
        type=float,
        default=0.0,
        help="Cache hit rate for Anthropic models (0.0-1.0, default: 0.0)"
    )

    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed breakdown"
    )

    args = parser.parse_args()

    # Validate cache hit rate
    if not 0.0 <= args.cache <= 1.0:
        print("Error: Cache hit rate must be between 0.0 and 1.0", file=sys.stderr)
        sys.exit(1)

    # Single model calculation
    if args.model and not args.compare:
        estimate = calculate_cost(
            model=args.model,
            input_tokens=args.input,
            output_tokens=args.output,
            requests=args.requests,
            cache_hit_rate=args.cache
        )
        print_estimate(estimate, detailed=args.detailed)

    # Comparison mode
    elif args.compare:
        models = args.models if args.models else list(PRICING.keys())

        estimates = compare_models(
            models=models,
            input_tokens=args.input,
            output_tokens=args.output,
            requests=args.requests,
            cache_hit_rate=args.cache
        )

        if args.detailed:
            for estimate in estimates:
                print_estimate(estimate, detailed=True)

        print_comparison(estimates)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
