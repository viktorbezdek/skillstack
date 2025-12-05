#!/usr/bin/env node

/**
 * Component Initialization Script
 *
 * Scaffolds new React/Vue components with accessibility and best practices built-in.
 *
 * Usage:
 *   npx tsx init-component.ts <component-name> [options]
 *
 * Options:
 *   --framework      Framework (react|vue) (default: react)
 *   --type           Component type (button|input|card|modal|dropdown|custom) (default: custom)
 *   --output-dir     Output directory (default: ./components)
 *   --typescript     Use TypeScript (default: true)
 *   --tests          Generate test file (default: true)
 *   --stories        Generate Storybook story (default: false)
 */

import * as fs from 'fs';
import * as path from 'path';

interface ComponentOptions {
  name: string;
  framework: 'react' | 'vue';
  type: 'button' | 'input' | 'card' | 'modal' | 'dropdown' | 'custom';
  outputDir: string;
  typescript: boolean;
  tests: boolean;
  stories: boolean;
}

function parseArgs(): ComponentOptions {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0].startsWith('--')) {
    console.error('Error: Component name is required');
    console.log('Usage: npx tsx init-component.ts <component-name> [options]');
    process.exit(1);
  }

  const options: ComponentOptions = {
    name: args[0],
    framework: 'react',
    type: 'custom',
    outputDir: './components',
    typescript: true,
    tests: true,
    stories: false,
  };

  for (let i = 1; i < args.length; i += 2) {
    const flag = args[i];
    const value = args[i + 1];

    switch (flag) {
      case '--framework':
        options.framework = value as 'react' | 'vue';
        break;
      case '--type':
        options.type = value as ComponentOptions['type'];
        break;
      case '--output-dir':
        options.outputDir = value;
        break;
      case '--typescript':
        options.typescript = value === 'true';
        break;
      case '--tests':
        options.tests = value === 'true';
        break;
      case '--stories':
        options.stories = value === 'true';
        break;
    }
  }

  return options;
}

function toPascalCase(str: string): string {
  return str
    .split(/[-_]/)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join('');
}

function generateReactComponent(options: ComponentOptions): string {
  const componentName = toPascalCase(options.name);
  const ext = options.typescript ? 'tsx' : 'jsx';

  const templates = {
    button: `import React from 'react';
${options.typescript ? "import type { ButtonHTMLAttributes, ReactNode } from 'react';" : ''}

${options.typescript ? `interface ${componentName}Props extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  children: ReactNode;
}` : ''}

export function ${componentName}({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  children,
  disabled,
  className = '',
  ...rest
}${options.typescript ? `: ${componentName}Props` : ''}) {
  const baseStyles = 'inline-flex items-center justify-center font-medium rounded-lg transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 disabled:opacity-50 disabled:cursor-not-allowed';

  const variantStyles = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus-visible:outline-blue-600',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
    ghost: 'bg-transparent hover:bg-gray-100',
  };

  const sizeStyles = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-6 py-3 text-base',
    lg: 'px-8 py-4 text-lg',
  };

  return (
    <button
      className={\`\${baseStyles} \${variantStyles[variant]} \${sizeStyles[size]} \${className}\`}
      disabled={disabled || isLoading}
      aria-busy={isLoading}
      {...rest}
    >
      {isLoading ? (
        <>
          <svg className="animate-spin -ml-1 mr-2 h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {children}
        </>
      ) : (
        children
      )}
    </button>
  );
}`,
    input: `import React, { useId } from 'react';
${options.typescript ? "import type { InputHTMLAttributes, ReactNode } from 'react';" : ''}

${options.typescript ? `interface ${componentName}Props extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  helperText?: string;
}` : ''}

export function ${componentName}({
  label,
  error,
  helperText,
  id,
  className = '',
  required,
  ...rest
}${options.typescript ? `: ${componentName}Props` : ''}) {
  const generatedId = useId();
  const inputId = id || generatedId;
  const errorId = \`\${inputId}-error\`;
  const helperId = \`\${inputId}-helper\`;

  return (
    <div className="space-y-1">
      <label htmlFor={inputId} className="block text-sm font-medium text-gray-700">
        {label}
        {required && <span className="text-red-500 ml-1" aria-label="required">*</span>}
      </label>

      <input
        id={inputId}
        className={\`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 \${
          error ? 'border-red-500 focus:ring-red-500' : 'border-gray-300'
        } \${className}\`}
        aria-invalid={error ? 'true' : 'false'}
        aria-describedby={error ? errorId : helperText ? helperId : undefined}
        required={required}
        {...rest}
      />

      {error && (
        <p id={errorId} className="text-sm text-red-600" role="alert">
          {error}
        </p>
      )}

      {helperText && !error && (
        <p id={helperId} className="text-sm text-gray-500">
          {helperText}
        </p>
      )}
    </div>
  );
}`,
    card: `import React from 'react';
${options.typescript ? "import type { ReactNode } from 'react';" : ''}

${options.typescript ? `interface ${componentName}Props {
  children: ReactNode;
  className?: string;
}` : ''}

export function ${componentName}({ children, className = '' }${options.typescript ? `: ${componentName}Props` : ''}) {
  return (
    <div className={\`bg-white rounded-lg border border-gray-200 shadow-sm \${className}\`}>
      {children}
    </div>
  );
}

export function ${componentName}Header({ children }${options.typescript ? `: ${componentName}Props` : ''}) {
  return <div className="px-6 py-4 border-b border-gray-200">{children}</div>;
}

export function ${componentName}Body({ children }${options.typescript ? `: ${componentName}Props` : ''}) {
  return <div className="px-6 py-4">{children}</div>;
}

export function ${componentName}Footer({ children }${options.typescript ? `: ${componentName}Props` : ''}) {
  return <div className="px-6 py-4 border-t border-gray-200 bg-gray-50">{children}</div>;
}`,
    modal: `import React, { useEffect, useRef } from 'react';
${options.typescript ? "import type { ReactNode } from 'react';" : ''}

${options.typescript ? `interface ${componentName}Props {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: ReactNode;
  size?: 'sm' | 'md' | 'lg';
}` : ''}

export function ${componentName}({
  isOpen,
  onClose,
  title,
  children,
  size = 'md',
}${options.typescript ? `: ${componentName}Props` : ''}) {
  const modalRef = useRef${options.typescript ? '<HTMLDivElement>' : ''}(null);

  useEffect(() => {
    if (!isOpen) return;

    function handleKeyDown(e${options.typescript ? ': KeyboardEvent' : ''}) {
      if (e.key === 'Escape') {
        onClose();
      }
    }

    document.addEventListener('keydown', handleKeyDown);

    // Focus first focusable element
    const focusable = modalRef.current?.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    if (focusable && focusable.length > 0) {
      (focusable[0] as HTMLElement).focus();
    }

    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const sizeClasses = {
    sm: 'w-full max-w-sm',
    md: 'w-full max-w-lg',
    lg: 'w-full max-w-2xl',
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black/50 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Modal */}
      <div
        ref={modalRef}
        className={\`relative bg-white rounded-lg shadow-xl max-h-[90vh] overflow-auto \${sizeClasses[size]}\`}
      >
        <div className="sticky top-0 bg-white border-b px-6 py-4 flex items-center justify-between">
          <h2 id="modal-title" className="text-xl font-semibold">
            {title}
          </h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded"
            aria-label="Close dialog"
          >
            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="px-6 py-4">{children}</div>
      </div>
    </div>
  );
}`,
    dropdown: `import React, { useState, useRef, useEffect } from 'react';
${options.typescript ? "import type { ReactNode } from 'react';" : ''}

${options.typescript ? `interface ${componentName}Props {
  trigger: ReactNode;
  children: ReactNode;
}

interface ${componentName}ItemProps {
  children: ReactNode;
  onClick?: () => void;
}` : ''}

export function ${componentName}({ trigger, children }${options.typescript ? `: ${componentName}Props` : ''}) {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef${options.typescript ? '<HTMLDivElement>' : ''}(null);

  useEffect(() => {
    function handleClickOutside(event${options.typescript ? ': MouseEvent' : ''}) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  return (
    <div className="relative" ref={menuRef}>
      <div onClick={() => setIsOpen(!isOpen)}>{trigger}</div>

      {isOpen && (
        <div
          className="absolute right-0 mt-2 w-56 bg-white rounded-lg shadow-lg border border-gray-200 z-10"
          role="menu"
          aria-orientation="vertical"
        >
          {children}
        </div>
      )}
    </div>
  );
}

export function ${componentName}Item({ children, onClick }${options.typescript ? `: ${componentName}ItemProps` : ''}) {
  return (
    <button
      className="w-full text-left px-4 py-2 hover:bg-gray-100 first:rounded-t-lg last:rounded-b-lg transition-colors"
      role="menuitem"
      onClick={onClick}
    >
      {children}
    </button>
  );
}`,
    custom: `import React from 'react';
${options.typescript ? "import type { ReactNode } from 'react';" : ''}

${options.typescript ? `interface ${componentName}Props {
  children?: ReactNode;
  className?: string;
}` : ''}

/**
 * ${componentName} component
 *
 * TODO: Add component description
 * TODO: Update props interface
 * TODO: Implement component logic
 */
export function ${componentName}({ children, className = '' }${options.typescript ? `: ${componentName}Props` : ''}) {
  return (
    <div className={\`${componentName.toLowerCase()} \${className}\`}>
      {children || 'TODO: Implement ${componentName}'}
    </div>
  );
}`,
  };

  return templates[options.type];
}

function generateTestFile(options: ComponentOptions): string {
  const componentName = toPascalCase(options.name);

  return `import { render, screen } from '@testing-library/react';
import { ${componentName} } from './${componentName}';

describe('${componentName}', () => {
  it('renders without crashing', () => {
    render(<${componentName}${options.type === 'input' ? ' label="Test"' : ''}${options.type === 'modal' ? ' isOpen={true} onClose={() => {}} title="Test"' : ''} />);
  });

  it('is accessible', async () => {
    const { container } = render(<${componentName}${options.type === 'input' ? ' label="Test"' : ''}${options.type === 'modal' ? ' isOpen={true} onClose={() => {}} title="Test"' : ''} />);
    // TODO: Add accessibility tests using jest-axe or similar
  });

  // TODO: Add more tests
});`;
}

function generateStoryFile(options: ComponentOptions): string {
  const componentName = toPascalCase(options.name);

  return `import type { Meta, StoryObj } from '@storybook/react';
import { ${componentName} } from './${componentName}';

const meta: Meta<typeof ${componentName}> = {
  title: 'Components/${componentName}',
  component: ${componentName},
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof ${componentName}>;

export const Default: Story = {
  args: {
    // TODO: Add default args
  },
};

// TODO: Add more stories
`;
}

function createComponent(options: ComponentOptions): void {
  const componentName = toPascalCase(options.name);
  const ext = options.typescript ? 'tsx' : 'jsx';
  const testExt = options.typescript ? 'tsx' : 'jsx';

  const componentDir = path.join(options.outputDir, componentName);

  // Create directory
  if (!fs.existsSync(componentDir)) {
    fs.mkdirSync(componentDir, { recursive: true });
  }

  // Generate component file
  const componentCode = generateReactComponent(options);
  const componentPath = path.join(componentDir, `${componentName}.${ext}`);
  fs.writeFileSync(componentPath, componentCode);
  console.log(`✓ Created component: ${componentPath}`);

  // Generate test file
  if (options.tests) {
    const testCode = generateTestFile(options);
    const testPath = path.join(componentDir, `${componentName}.test.${testExt}`);
    fs.writeFileSync(testPath, testCode);
    console.log(`✓ Created test file: ${testPath}`);
  }

  // Generate story file
  if (options.stories) {
    const storyCode = generateStoryFile(options);
    const storyPath = path.join(componentDir, `${componentName}.stories.${ext}`);
    fs.writeFileSync(storyPath, storyCode);
    console.log(`✓ Created story file: ${storyPath}`);
  }

  // Generate index file
  const indexPath = path.join(componentDir, 'index.ts');
  fs.writeFileSync(indexPath, `export { ${componentName} } from './${componentName}';\n`);
  console.log(`✓ Created index: ${indexPath}`);

  // Generate README
  const readmePath = path.join(componentDir, 'README.md');
  const readme = `# ${componentName}

## Usage

\`\`\`${ext}
import { ${componentName} } from '@/components/${componentName}';

function Example() {
  return (
    <${componentName}${options.type === 'input' ? ' label="Email" name="email"' : ''}${options.type === 'modal' ? ' isOpen={true} onClose={() => {}} title="Modal Title"' : ''}>
      ${options.type === 'button' ? 'Click me' : 'Content'}
    </${componentName}>
  );
}
\`\`\`

## Props

TODO: Document props

## Accessibility

This component follows WCAG 2.2 guidelines and includes:
- Semantic HTML
- Keyboard navigation support
- Screen reader support
- Focus management

## Examples

TODO: Add usage examples
`;
  fs.writeFileSync(readmePath, readme);
  console.log(`✓ Created README: ${readmePath}`);
}

function main() {
  const options = parseArgs();

  console.log(`\\n🚀 Initializing ${options.framework} component: ${options.name}`);
  console.log(`   Type: ${options.type}`);
  console.log(`   TypeScript: ${options.typescript}`);
  console.log(`   Tests: ${options.tests}`);
  console.log(`   Stories: ${options.stories}\\n`);

  if (options.framework !== 'react') {
    console.error('❌ Error: Only React is currently supported');
    console.log('Vue support coming soon!');
    process.exit(1);
  }

  try {
    createComponent(options);
    console.log(`\\n✅ Component created successfully!`);
    console.log(`\\nNext steps:`);
    console.log(`  1. Review and customize the generated component`);
    console.log(`  2. Add or update component props as needed`);
    console.log(`  3. Implement component-specific logic`);
    console.log(`  4. Write comprehensive tests`);
    console.log(`  5. Test with screen readers and keyboard navigation\\n`);
  } catch (error) {
    console.error('❌ Error creating component:', error);
    process.exit(1);
  }
}

main();
