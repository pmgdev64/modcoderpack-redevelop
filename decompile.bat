@echo off
chcp 65001 > nul

echo [MCP 9.51] Đang khởi chạy Decompile (Chế độ tối ưu RAM)...
echo Toàn bộ log chi tiết đang được ghi vào: decompile_results.log

:: Sử dụng lệnh chuyển hướng để RAM không phải gánh buffer hiển thị
py -3 runtime\decompile.py %* > decompile_results.log 2>&1

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Có lỗi xảy ra. Hãy kiểm tra file decompile_results.log để biết chi tiết.
) else (
    echo.
    echo [SUCCESS] Quá trình hoàn tất thành công!
)
pause