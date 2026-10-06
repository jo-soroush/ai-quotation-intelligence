import { expect, test } from "@playwright/test";

test("synthetic request reaches real evidence, approval, and backend Excel download", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByText("Local synthetic demo")).toBeVisible();
  await page.getByRole("button", { name: "Load synthetic example" }).click();
  await expect(page.getByRole("group")).toHaveCount(3);
  await page.getByRole("button", { name: "Analyze & create draft" }).click();

  await expect(page.getByRole("heading", { name: "Draft intelligence" })).toBeVisible();
  await expect(page.getByLabel("Backend-calculated quotation total")).toContainText("4620 SEK");
  await expect(page.getByRole("heading", { name: "Comparable quotations" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Estimate vs actual" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Risk evidence" })).toBeVisible();
  await expect(page.getByText("AI-selected interpretation")).toBeVisible();

  const downloadButton = page.getByRole("button", { name: "Download Excel quotation" });
  await expect(downloadButton).toBeDisabled();
  await page.getByRole("button", { name: "Approve quotation" }).click();
  await page.getByRole("button", { name: "Confirm approval" }).click();
  await expect(page.getByText(/Decision recorded by the backend: approved/)).toBeVisible();
  await expect(downloadButton).toBeEnabled();

  const downloadPromise = page.waitForEvent("download");
  await downloadButton.click();
  const download = await downloadPromise;
  expect(download.suggestedFilename()).toBe("Draft_Quote.xlsx");
  await expect(page.getByText(/genuine backend-generated Excel quotation was downloaded/i)).toBeVisible();
});

test("pre-approval restriction and real provider failure are presented honestly", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Load synthetic example" }).click();
  await page.getByLabel("Project name").fill("Synthetic Provider Failure");
  await page.getByRole("button", { name: "Analyze & create draft" }).click();
  await expect(page.getByText(/AI provider is unavailable/)).toBeVisible();
  await expect(page.getByText(/No successful draft was created/)).toBeVisible();
  await expect(page.getByRole("heading", { name: "Draft intelligence" })).toHaveCount(0);
});
