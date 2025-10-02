# Component Patterns

Comprehensive guide to creating reusable, maintainable UI components with modern patterns and best practices (2025).

## Component Design Principles

### Single Responsibility

Each component should have one clear purpose.

**Good - focused component:**
```typescript
// Button.tsx - Only handles button rendering and interaction
interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export function Button({ children, onClick, variant = 'primary', disabled }: ButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`btn btn-${variant}`}
    >
      {children}
    </button>
  );
}
```

**Bad - too many responsibilities:**
```typescript
// UserProfile.tsx - Handles data fetching, validation, AND rendering
function UserProfile({ userId }: { userId: string }) {
  // Data fetching (should be in a hook)
  // Form validation (should be in a hook)
  // Complex rendering logic (should be split into smaller components)
}
```

### Composition Over Configuration

Prefer composable components over highly configurable ones.

**Good - composition:**
```typescript
// Card.tsx
export function Card({ children }: { children: React.ReactNode }) {
  return <div className="card">{children}</div>;
}

export function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="card-header">{children}</div>;
}

export function CardBody({ children }: { children: React.ReactNode }) {
  return <div className="card-body">{children}</div>;
}

// Usage
<Card>
  <CardHeader>
    <h2>Title</h2>
  </CardHeader>
  <CardBody>
    <p>Content</p>
  </CardBody>
</Card>
```

**Bad - excessive configuration:**
```typescript
<Card
  title="Title"
  titleLevel={2}
  showHeader={true}
  headerAlign="left"
  body="Content"
  showFooter={false}
  footerAlign="right"
/>
```

### Controlled vs Uncontrolled

Choose the appropriate pattern for state management.

**Controlled component** (parent manages state):
```typescript
function ControlledInput() {
  const [value, setValue] = useState('');

  return (
    <input
      value={value}
      onChange={(e) => setValue(e.target.value)}
    />
  );
}
```

**Uncontrolled component** (component manages state):
```typescript
function UncontrolledInput() {
  const inputRef = useRef<HTMLInputElement>(null);

  function handleSubmit() {
    console.log(inputRef.current?.value);
  }

  return <input ref={inputRef} />;
}
```

**Hybrid approach** (support both):
```typescript
interface InputProps {
  value?: string; // Controlled
  defaultValue?: string; // Uncontrolled
  onChange?: (value: string) => void;
}

function Input({ value, defaultValue, onChange }: InputProps) {
  const [internalValue, setInternalValue] = useState(defaultValue || '');
  const isControlled = value !== undefined;
  const currentValue = isControlled ? value : internalValue;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value;
    if (!isControlled) {
      setInternalValue(newValue);
    }
    onChange?.(newValue);
  };

  return <input value={currentValue} onChange={handleChange} />;
}
```

## Props Design

### Props Naming

Use clear, consistent naming conventions.

**Good naming:**
```typescript
interface ButtonProps {
  // Boolean props: is/has/should prefix
  isLoading?: boolean;
  isDisabled?: boolean;
  hasIcon?: boolean;

  // Event handlers: on prefix
  onClick?: () => void;
  onHover?: () => void;
  onFocus?: () => void;

  // Variants: clear enumeration
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';

  // Content: descriptive names
  children: React.ReactNode;
  icon?: React.ReactNode;
  label?: string;
}
```

### Optional vs Required Props

Make intentions clear through types.

```typescript
// Required props have no default or undefined
interface RequiredProps {
  title: string; // Required
  userId: string; // Required
}

// Optional props use ?
interface OptionalProps {
  subtitle?: string; // Optional
  className?: string; // Optional
  variant?: 'light' | 'dark'; // Optional, no default shown
}

// Default values shown in implementation
function Component({ variant = 'light' }: OptionalProps) {
  // variant is 'light' if not provided
}
```

### Prop Spreading

Use prop spreading judiciously.

**Good - spreading rest props to DOM element:**
```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
}

function Button({ variant = 'primary', children, ...rest }: ButtonProps) {
  return (
    <button className={`btn-${variant}`} {...rest}>
      {children}
    </button>
  );
}

// Supports all native button props
<Button onClick={...} disabled aria-label="...">Click me</Button>
```

**Bad - uncontrolled prop spreading:**
```typescript
function Component(props: any) {
  return <div {...props} />; // No type safety
}
```

## Styling Approaches

### CSS Modules

Scoped styles with local class names.

**Button.module.css:**
```css
.button {
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
}

.primary {
  background: var(--color-primary);
  color: white;
}

.secondary {
  background: transparent;
  border: 1px solid var(--color-border);
}
```

**Button.tsx:**
```typescript
import styles from './Button.module.css';

function Button({ variant = 'primary' }: ButtonProps) {
  return (
    <button className={`${styles.button} ${styles[variant]}`}>
      Click me
    </button>
  );
}
```

### Tailwind CSS

Utility-first styling.

```typescript
function Button({ variant = 'primary' }: ButtonProps) {
  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'bg-transparent border border-gray-300 hover:bg-gray-50',
  };

  return (
    <button
      className={`px-6 py-3 rounded-lg font-medium ${variants[variant]}`}
    >
      Click me
    </button>
  );
}
```

### CSS-in-JS (Styled Components)

Component-scoped styles with JavaScript.

```typescript
import styled from 'styled-components';

const StyledButton = styled.button<{ $variant: 'primary' | 'secondary' }>`
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;

  ${(props) =>
    props.$variant === 'primary'
      ? `
        background: var(--color-primary);
        color: white;
      `
      : `
        background: transparent;
        border: 1px solid var(--color-border);
      `}
`;

function Button({ variant = 'primary' }: ButtonProps) {
  return <StyledButton $variant={variant}>Click me</StyledButton>;
}
```

### Style Composition (clsx/classnames)

Combine class names conditionally.

```typescript
import clsx from 'clsx';

function Button({ variant, size, isLoading, className }: ButtonProps) {
  return (
    <button
      className={clsx(
        // Base styles
        'font-medium rounded-lg transition-colors',
        // Variant styles
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-transparent border border-gray-300': variant === 'secondary',
        },
        // Size styles
        {
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-6 py-3 text-base': size === 'md',
          'px-8 py-4 text-lg': size === 'lg',
        },
        // State styles
        {
          'opacity-50 cursor-not-allowed': isLoading,
        },
        // Custom className
        className
      )}
    >
      Click me
    </button>
  );
}
```

## Common Component Patterns

### Button Component

Full-featured button with variants, sizes, and states.

```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right';
}

export function Button({
  children,
  variant = 'primary',
  size = 'md',
  isLoading = false,
  icon,
  iconPosition = 'left',
  disabled,
  className,
  ...rest
}: ButtonProps) {
  return (
    <button
      className={clsx(
        'inline-flex items-center justify-center gap-2 font-medium rounded-lg transition-colors',
        'focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2',
        'disabled:opacity-50 disabled:cursor-not-allowed',
        {
          'bg-blue-600 text-white hover:bg-blue-700 focus-visible:outline-blue-600': variant === 'primary',
          'bg-gray-200 text-gray-900 hover:bg-gray-300': variant === 'secondary',
          'bg-transparent hover:bg-gray-100': variant === 'ghost',
          'bg-red-600 text-white hover:bg-red-700 focus-visible:outline-red-600': variant === 'danger',
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-6 py-3 text-base': size === 'md',
          'px-8 py-4 text-lg': size === 'lg',
        },
        className
      )}
      disabled={disabled || isLoading}
      {...rest}
    >
      {isLoading ? (
        <span className="animate-spin">⏳</span>
      ) : icon && iconPosition === 'left' ? (
        icon
      ) : null}
      {children}
      {!isLoading && icon && iconPosition === 'right' ? icon : null}
    </button>
  );
}
```

### Input Component

Accessible form input with label and error state.

```typescript
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  helperText?: string;
}

export function Input({
  label,
  error,
  helperText,
  id,
  className,
  ...rest
}: InputProps) {
  const inputId = id || useId();
  const errorId = `${inputId}-error`;
  const helperId = `${inputId}-helper`;

  return (
    <div className="space-y-1">
      <label htmlFor={inputId} className="block text-sm font-medium text-gray-700">
        {label}
        {rest.required && <span className="text-red-500 ml-1">*</span>}
      </label>

      <input
        id={inputId}
        className={clsx(
          'w-full px-4 py-2 border rounded-lg',
          'focus:outline-none focus:ring-2 focus:ring-blue-500',
          error
            ? 'border-red-500 focus:ring-red-500'
            : 'border-gray-300',
          className
        )}
        aria-invalid={error ? 'true' : 'false'}
        aria-describedby={clsx(error && errorId, helperText && helperId)}
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
}
```

### Modal Component

Accessible modal with focus trap and backdrop.

```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
  size?: 'sm' | 'md' | 'lg';
}

export function Modal({ isOpen, onClose, title, children, size = 'md' }: ModalProps) {
  useEffect(() => {
    if (!isOpen) return;

    // Trap focus
    const focusableElements = document.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0] as HTMLElement;
    const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') {
        onClose();
      } else if (e.key === 'Tab') {
        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        } else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
    }

    document.addEventListener('keydown', handleKeyDown);
    firstElement?.focus();

    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black/50 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div
        className={clsx(
          'relative bg-white rounded-lg shadow-xl max-h-[90vh] overflow-auto',
          {
            'w-full max-w-sm': size === 'sm',
            'w-full max-w-lg': size === 'md',
            'w-full max-w-2xl': size === 'lg',
          }
        )}
      >
        <div className="sticky top-0 bg-white border-b px-6 py-4 flex items-center justify-between">
          <h2 id="modal-title" className="text-xl font-semibold">
            {title}
          </h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600"
            aria-label="Close dialog"
          >
            ✕
          </button>
        </div>

        <div className="px-6 py-4">{children}</div>
      </div>
    </div>
  );
}
```

### Card Component

Composable card with header, body, and footer.

```typescript
export function Card({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={clsx('bg-white rounded-lg border border-gray-200 shadow-sm', className)}>
      {children}
    </div>
  );
}

export function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="px-6 py-4 border-b border-gray-200">{children}</div>;
}

export function CardBody({ children }: { children: React.ReactNode }) {
  return <div className="px-6 py-4">{children}</div>;
}

export function CardFooter({ children }: { children: React.ReactNode }) {
  return <div className="px-6 py-4 border-t border-gray-200 bg-gray-50">{children}</div>;
}

// Usage
<Card>
  <CardHeader>
    <h3 className="text-lg font-semibold">Card Title</h3>
  </CardHeader>
  <CardBody>
    <p>Card content goes here</p>
  </CardBody>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>
```

### Dropdown Menu Component

Accessible dropdown with keyboard navigation.

```typescript
export function DropdownMenu({ trigger, children }: {
  trigger: React.ReactNode;
  children: React.ReactNode;
}) {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
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
        >
          {children}
        </div>
      )}
    </div>
  );
}

export function DropdownMenuItem({ children, onClick }: {
  children: React.ReactNode;
  onClick?: () => void;
}) {
  return (
    <button
      className="w-full text-left px-4 py-2 hover:bg-gray-100 first:rounded-t-lg last:rounded-b-lg"
      role="menuitem"
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

## Advanced Patterns

### Compound Components

Components that work together with shared state.

```typescript
interface TabsContextValue {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

const TabsContext = React.createContext<TabsContextValue | null>(null);

export function Tabs({ defaultTab, children }: {
  defaultTab: string;
  children: React.ReactNode;
}) {
  const [activeTab, setActiveTab] = useState(defaultTab);

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div>{children}</div>
    </TabsContext.Provider>
  );
}

export function TabList({ children }: { children: React.ReactNode }) {
  return (
    <div role="tablist" className="flex gap-2 border-b">
      {children}
    </div>
  );
}

export function Tab({ value, children }: { value: string; children: React.ReactNode }) {
  const context = useContext(TabsContext);
  if (!context) throw new Error('Tab must be used within Tabs');

  const { activeTab, setActiveTab } = context;
  const isActive = activeTab === value;

  return (
    <button
      role="tab"
      aria-selected={isActive}
      onClick={() => setActiveTab(value)}
      className={clsx(
        'px-4 py-2 font-medium border-b-2 transition-colors',
        isActive
          ? 'border-blue-600 text-blue-600'
          : 'border-transparent text-gray-600 hover:text-gray-900'
      )}
    >
      {children}
    </button>
  );
}

export function TabPanel({ value, children }: { value: string; children: React.ReactNode }) {
  const context = useContext(TabsContext);
  if (!context) throw new Error('TabPanel must be used within Tabs');

  const { activeTab } = context;
  if (activeTab !== value) return null;

  return (
    <div role="tabpanel" className="p-4">
      {children}
    </div>
  );
}

// Usage
<Tabs defaultTab="profile">
  <TabList>
    <Tab value="profile">Profile</Tab>
    <Tab value="settings">Settings</Tab>
  </TabList>
  <TabPanel value="profile">Profile content</TabPanel>
  <TabPanel value="settings">Settings content</TabPanel>
</Tabs>
```

### Render Props

Share logic through function props.

```typescript
interface MousePositionProps {
  children: (position: { x: number; y: number }) => React.ReactNode;
}

function MousePosition({ children }: MousePositionProps) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    function handleMouseMove(e: MouseEvent) {
      setPosition({ x: e.clientX, y: e.clientY });
    }

    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return <>{children(position)}</>;
}

// Usage
<MousePosition>
  {({ x, y }) => (
    <div>
      Mouse position: {x}, {y}
    </div>
  )}
</MousePosition>
```

### Polymorphic Components

Components that can render as different elements.

```typescript
type AsProp<C extends React.ElementType> = {
  as?: C;
};

type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);

type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, PropsToOmit<C, Props>>;

type TextProps<C extends React.ElementType> = PolymorphicComponentProp<
  C,
  { color?: 'primary' | 'secondary' }
>;

export function Text<C extends React.ElementType = 'span'>({
  as,
  color = 'primary',
  children,
  ...rest
}: TextProps<C>) {
  const Component = as || 'span';

  return (
    <Component
      className={clsx({
        'text-blue-600': color === 'primary',
        'text-gray-600': color === 'secondary',
      })}
      {...rest}
    >
      {children}
    </Component>
  );
}

// Usage
<Text>Default span</Text>
<Text as="p">Paragraph</Text>
<Text as="h1" color="primary">Heading</Text>
```

## Best Practices

1. **Type safety**: Use TypeScript for prop definitions
2. **Accessibility**: Include ARIA attributes and keyboard support
3. **Composition**: Prefer small, composable components
4. **Consistent API**: Follow established patterns across components
5. **Documentation**: Add JSDoc comments for complex props
6. **Testing**: Write unit tests for component logic
7. **Performance**: Use React.memo for expensive components
8. **Error boundaries**: Handle errors gracefully
9. **Default props**: Provide sensible defaults
10. **Extensibility**: Support className and style props for customization
