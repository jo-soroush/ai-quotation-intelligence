import "@testing-library/jest-dom/vitest";
import { afterEach, vi } from "vitest";
import { cleanup } from "@testing-library/react";

afterEach(() => cleanup());

Object.defineProperty(URL, "createObjectURL", { configurable: true, value: vi.fn(() => "blob:c20-workbook") });
Object.defineProperty(URL, "revokeObjectURL", { configurable: true, value: vi.fn() });
Object.defineProperty(HTMLAnchorElement.prototype, "click", { configurable: true, value: vi.fn() });
