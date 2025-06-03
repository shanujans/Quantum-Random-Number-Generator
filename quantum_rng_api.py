# quantum_rng_api.py
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
import time

# Load environment variables from .env file
load_dotenv()

def init_ibm_service():
    try:
        api_key = os.getenv("IBM_API_KEY")
        if not api_key:
            print("❌ IBM_API_KEY not found in .env file")
            return None

        instance_name = "Quantum_rng"
        service = QiskitRuntimeService(
            channel="ibm_cloud",
            token=api_key,
            instance=instance_name
        )
        print("✅ Connected to IBM Quantum Cloud")
        print(f"ℹ️ Using IBM Quantum instance: {instance_name}")
        return service
    except Exception as e:
        print(f"❌ IBM Connection failed: {str(e)}")
        return None

def get_quantum_backend(service):
    """Get an operational quantum backend from the IBM Quantum service."""
    try:
        try:
            backend = service.backend("ibm_sherbrooke")
            if backend.status().operational:
                print("🔧 Selected quantum processor: ibm_sherbrooke")
                return backend
        except Exception:
            pass # ibm_sherbrooke might not be available or operational

        print("🔍 Searching for operational backends...")
        for backend in service.backends():
            if backend.status().operational:
                print(f"🔧 Selected backend: {backend.name}")
                return backend

        print("⚠️ No operational IBM backends found")
        return None
    except Exception as e:
        print(f"❌ Backend selection failed: {str(e)}")
        return None

def run_quantum_job(backend, n_bits):
    """Run a quantum job on IBM quantum hardware."""
    try:
        qc = QuantumCircuit(n_bits)
        qc.h(range(n_bits))
        qc.measure_all()

        qc_transpiled = transpile(qc, backend)

        sampler = Sampler(backend)
        job = sampler.run([qc_transpiled], shots=1)
        job_id = job.job_id()
        print(f"🚀 Job submitted. ID: {job_id}")
        print(f"🔗 Monitor at: https://quantum.ibm.com/jobs/{job_id}")

        start_time = time.time()
        result = job.result()
        exec_time = time.time() - start_time
        
        bits = None # Initialize bits to None

        # Access results via the identified working internal path
        if hasattr(result, '_pub_results') and result._pub_results:
            try:
                pub_result_item = result._pub_results[0]
                
                if hasattr(pub_result_item, 'data') and pub_result_item.data:
                    internal_data_bin = pub_result_item.data

                    if hasattr(internal_data_bin, 'meas') and internal_data_bin.meas is not None:
                        bit_array_result = internal_data_bin.meas

                        # Use get_bitstrings() to extract the measurement result
                        bitstrings_list = bit_array_result.get_bitstrings()
                        if bitstrings_list:
                            bits = bitstrings_list[0]
                        else:
                            print("❌ Quantum job failed: get_bitstrings() returned an empty list.")
                        
                        if bits:
                            print(f"🎉 Quantum generation successful in {exec_time:.2f}s")
                            return bits
                        else:
                            print("❌ Quantum job failed: Could not extract bit string from BitArray.")
                            return None
                    else:
                        print("❌ Quantum job failed: '_pub_results[0].data' does not contain 'meas' attribute or it's empty.")
                else:
                    print("❌ Quantum job failed: '_pub_results[0]' does not have a 'data' attribute or it's empty.")
            except (AttributeError, IndexError, KeyError) as e:
                print(f"❌ Quantum job failed: Error accessing result from '_pub_results': {str(e)}")
        else:
            print("❌ Quantum job failed: Neither 'data' nor '_pub_results' attribute found on the result object.")

        return None # Return None if bits could not be extracted

    except Exception as e:
        print(f"❌ Quantum job failed: {str(e)}")
        return None

def run_local_simulation(n_bits):
    """Run a local quantum simulation as a fallback."""
    print("⚛️ Using local quantum simulator...")
    simulator = AerSimulator()
    qc = QuantumCircuit(n_bits)
    qc.h(range(n_bits))
    qc.measure_all()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()
    bits = next(iter(counts.keys())).replace(" ", "")
    print("🏁 Local simulator successful!")
    return bits

def generate_quantum_bits(n_bits):
    """Main function to generate quantum bits either from hardware or locally."""
    service = init_ibm_service()
    if not service:
        return run_local_simulation(n_bits)

    backend = get_quantum_backend(service)
    if not backend:
        return run_local_simulation(n_bits)
    
    bits = run_quantum_job(backend, n_bits)
    if bits:
        return bits

    # Fallback to local simulation if quantum job fails.
    return run_local_simulation(n_bits)

if __name__ == "__main__":
    print("=== Quantum Random Number Generator ===")
    try:
        n_bits = int(input("Enter number of bits (8-256): "))
        n_bits = max(8, min(256, n_bits))
    except Exception:
        n_bits = 8
        print("Invalid input: Using default 8 bits")

    bits = generate_quantum_bits(n_bits)
    print(f"\nRandom bits: {bits}")
    print(f"Decimal value: {int(bits, 2)}")

    # Additional verification.
    print("\nQuantum properties:")
    zeros = bits.count('0')
    ones = bits.count('1')
    print(f"Bit distribution: {zeros} zeros, {ones} ones")
    # A simple entropy test: bits should be somewhat evenly distributed
    ratio = ones / n_bits
    print(f"Entropy test: {'Pass' if 0.4 < ratio < 0.6 else 'Fail'}")
